Write-Output 'Definindo variáveis de ambiente'

# SECRET_KEY gerado em https://djecrety.ir/
$env:DJANGO_SECRET_KEY = 'ia0o-8x75=29v*oxbr=07rv1w_3+^_8ol8o-m8^w8%o@r!4h5u'

Write-Output 'Apagando arquivos *.pyc em todos os subdiretórios'
Remove-Item -Path . -Filter *.pyc -Recurse -Force
Remove-Item -Path . -Filter *.pyo -Recurse -Force

Write-Output 'Apagando diretório __pycache__ em todos os subdiretórios'
Remove-Item -Path . -Filter __pycache__ -Recurse -Force
