import boto3

polly = boto3.client('polly', 
    region_name = 'sa-east-1')

result = polly.synthesize_speech(Text='Hola!', OutputFormat='mp3', VoiceId='Mia')

audio = result['AudioStream'].read()
with open('polly-hello.mp3', 'wb') as file:
    file.write(audio)