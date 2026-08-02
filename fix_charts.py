import os
os.chdir(r'C:\Users\Administrator\middleware')

with open('nacos/values.yaml') as f:
    n = f.read()
if 'auth:' not in n:
    n += '\nauth:\n  token: "VGhpc0lzTXlOYW1lc0F1dGhUb2tlbkZvck5hY29z"\n  identityKey: "serverIdentity"\n  identityValue: "nacos-server"\n'
open('nacos/values.yaml','w').write(n)

with open('nacos/templates/deployment.yaml') as f:
    d = f.read()
if 'NACOS_AUTH_TOKEN' not in d:
    d = d.replace('          resources:', '''            - name: NACOS_AUTH_TOKEN
              value: "{{ .Values.auth.token }}"
            - name: NACOS_AUTH_IDENTITY_KEY
              value: "{{ .Values.auth.identityKey }}"
            - name: NACOS_AUTH_IDENTITY_VALUE
              value: "{{ .Values.auth.identityValue }}"
          resources:''')
open('nacos/templates/deployment.yaml','w').write(d)

r = open('rabbitmq/values.yaml').read()
r = r.replace('tag: 3.9.2', 'tag: 3.13.0-management-alpine')
open('rabbitmq/values.yaml','w').write(r)

l = open('litellm/values.yaml').read()
l = l.replace('memory: 1Gi', 'memory: 2Gi')
open('litellm/values.yaml','w').write(l)

print('ALL FIXED')
