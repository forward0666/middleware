{{- define "omniroute.name" -}}omniroute{{- end -}}
{{- define "omniroute.fullname" -}}omniroute{{- end -}}
{{- define "omniroute.labels" -}}
app: {{ include "omniroute.name" . }}
app.kubernetes.io/name: {{ include "omniroute.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
helm.sh/chart: {{ printf "%s-%s" .Chart.Name .Chart.Version }}
{{- end -}}
{{- define "omniroute.redisLabels" -}}
app: omniroute-redis
app.kubernetes.io/name: omniroute-redis
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
helm.sh/chart: {{ printf "%s-%s" .Chart.Name .Chart.Version }}
{{- end -}}
