import sys
import json
import base64
import requests
import webbrowser
import wave, pyaudio
import os
import time
import ybc_pinyin


def voice2text(filename='', rate=16000,format_type=2):
    '''语音转文字'''
    if not filename:
        return -1

    if rate in (0, 1, 8000, 16000):
        rate = 1
    else:
        rate = 1

    if format_type not in (1, 2, 3, 4):
        format_type = 'PCM'
    else:
        format_type = 'PCM'

    url = 'https://www.yuanfudao.com/tutor-ybc-course-api-v2/api/speech'
    filepath = os.path.abspath(filename)
    data = {}
    data['format'] = format_type
    data['sampleRate'] = rate
    files = {
        'file': open(filepath, 'rb')
    }

    for i in range(3):
        r = requests.post(url, data=data, files=files)
        if r.status_code == 200:
            res = r.json()
            return res['data']
        elif i < 2:
            continue
        else:
            raise ConnectionError('转换语音文件失败', r._content)

def text2voice(text, filename,model_type=2,speed=0):
    '''文字转语音'''
    if not filename or not text:
        return -1
    if model_type not in (0,1,2,3) :
        model_type = 2
    elif model_type == 3 :
        model_type = 6

    if speed == 0.6 :
        speed = -2
    elif speed == 0.8 :
        speed = -1
    elif speed == 0 :
        speed = 0
    elif speed == 1.2 :
        speed = 1
    elif speed == 1.5 :
        speed = 2
    else :
        speed = 0
    url = 'https://www.yuanfudao.com/tutor-ybc-course-api/text2voice.php'
    data = {}
    data['text'] = text
    data['model_type'] = model_type
    data['speed'] = speed
    r = requests.post(url, data=data)
    res = r.json()
    if res['ret'] == 0 and res['data'] :
        b64_data = base64.b64decode(res['data']['voice'])
        with open(filename,'wb') as f:
            f.write(b64_data)
    return filename

def record(filename, seconds=5, rate=16000, channels=1, chunk=1024):
    '''录制音频采样率16000'''
    if not filename:
        return -1

    # if to_dir is None:
        # to_dir = "./"
        # to_dir = ''

    pa = pyaudio.PyAudio()
    stream = pa.open(format = pyaudio.paInt16,
                     channels = channels,
                     rate = rate,
                     input = True,
                     frames_per_buffer = chunk)

    print("* 你要做点啥？(#^.^#)")

    save_buffer = []
    for i in range(0, int(rate / chunk * seconds)):
        audio_data = stream.read(chunk)
        save_buffer.append(audio_data)


    # stop
    stream.stop_stream()
    stream.close()
    pa.terminate()

    # if to_dir.endswith('/'):
    #     file_path = to_dir + filename
    # else:
    #     file_path = to_dir + "/" + filename
    file_path = filename

    # save file
    wf = wave.open(file_path, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(pa.get_sample_size(pyaudio.paInt16,))
    wf.setframerate(rate)
    # join 前的类型
    wf.writeframes(b''.join(save_buffer))
    wf.close()

    return file_path

def _speak(text='',model_type=2,speed=0):
    '''朗读'''
    if text:
        filename = str(int(time.time())) + '_tmp.wav'
        res1 = text2voice(text,filename,model_type,speed)
    if len(text) <= 10:
        time.sleep(6)
    else :
        time.sleep(8)
    os.system(filename)

def text2voice1(text, filename,speaker=1,speed=1,aht=0,apc=58,volume=10,_format=2):
    '''文字转语音'''
    if not filename or not text:
        return -1
    if speaker  == 2:
        speaker = 5
    elif speaker == 3:
        speaker =6
    elif speaker == 4:
        speaker = 7
    else :
        speaker = 1

    if speed == 1 :
        speed = 100
    elif speed == 0.5 :
        speed = 50
    elif speed == 1.5 :
        speed =150
    elif speed == 2 :
        speed = 200
    else :
        speed = 100

    url = 'https://www.yuanfudao.com/tutor-ybc-course-api/text2voice1.php'
    #aht = 0 # -24~24 合成语音降低/升高半音个数，即改变音高，默认0
    #apc = 58 # 0~100 控制频谱翘曲的程度，改变说话人的音色，默认58
    data = {}
    data['text'] = text
    data['speaker'] = speaker
    data['speed'] = speed
    data['volume'] = volume
    data['format'] = _format
    data['aht'] = aht
    data['apc'] = apc
    r = requests.post(url, data=data)
    res = r.json()
    if res['ret'] == 0 and res['data'] :
        b64_data = base64.b64decode(res['data']['speech'])
        with open(filename,'wb') as f:
            f.write(b64_data)
    return filename

def speak(text='',speaker=1,speed=1,aht=0,apc=58):
    '''朗读'''
    if text:
        filename = str(int(time.time())) + '_tmp.wav'
        res1 = text2voice1(text,filename,speaker,speed,aht,apc)
    os.system(filename)
    if len(text) <= 10:
        time.sleep(4)
    elif len(text) <= 20:
        time.sleep(5)
    elif len(text) <= 30 :
        time.sleep(6)
    elif len(text) <= 40 :
        time.sleep(7)

def todo():
    file_path = record('tmp.wav',4)
    text = voice2text(file_path)
    open_browser(text)


''' 打开指定网址'''
def open_browser(text):
    urls = {
        'baidu':'http://www.baidu.com',
        'yuanfudao':'http://yuanfudao.com',
        'xiaoyuan':'http://www.yuanfudao.com/info/emojis',
        'sougou':'http://www.sogou.com',
    	'sanliuling':'http://www.so.com',
    	'shipin':'http://v.qq.com',
    	'youxi':'http://www.4399.com',
    	'yinyue':'http://music.163.com',
    	'donghua':'http://child.iqiyi.com',
    	'dianying':'http://www.iqiyi.com/dianying/',
        'biancheng':'https://python.yuanfudao.com/',
        'shuai':'https://www.yuanfudao.com/tutor-ybc-course-api/fshow/king1.jpg'
    }
    if not text:
        return -1
    res = ybc_pinyin.pin1(text)
    res = res.replace('-','')

    if 'baidu' in res:
        url = urls['baidu']
    elif 'yuanfudao' in res:
        url = urls['yuanfudao']
    elif 'xiaoyuan' in res:
        url = urls['xiaoyuan']
    elif 'sougou' in res:
        url = urls['sougou']
    elif 'sanliuling' in res:
        url = urls['sanliuling']
    elif 'shipin' in res:
        url = urls['shipin']
    elif 'youxi' in res:
        url = urls['youxi']
    elif 'yinyue' in res:
        url = urls['yinyue']
    elif 'donghua' in res:
        url = urls['donghua']
    elif 'dianying' in res:
        url = urls['dianying']
    elif 'biancheng' in res:
        url = urls['biancheng']
    elif 'shuai' in res:
        url = urls['shuai']
    else:
        url = "http://www.baidu.com"
    return webbrowser.open_new_tab(url)


def main():
    # speak('大家好欢迎莱奥原')
    # print(text2voice1('我不管我最帅我是你们的小可爱'*3,'2.wav',4,1,-12,50))
    # text2voice1('大家好，欢迎来到猿辅导','2333.wav',2)
    todo()

if __name__ == '__main__':
    main()
