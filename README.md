# Pratica #6 - Visão computacional, sistema de controle de versão e APIs públicas

> SEL0337 - Aplicação de Microprocessadores II  
> Prof. Pedro de Oliveira Conceição Junior  
>
> Felipe Pimenta Bernardo - 10788697  
> Flávio Alegretti Ramos - 10748434

---

## Objetivos

O objetivo desta prática era gerar um script em python que cumprisse duas tarefas: 
- Acessar a câmera conectada à Rasp;
- Obter informações de uma API climática.

## Bibliotecas utilizadas

Para isso, o primeiro passo foi instalar e importar as bibliotecas necessárias.  
O método `get` importado da biblioteca `requests` foi usado para fazer requisições à API climática. Uma vez que as requisições transmitem informações em seu corpo através de um objeto JavaScript, ou **JSON** (JavaScript Object Notation), foi utilizada também a biblioteca `json` para conversão desse objeto JavaScript em um dicionário Python. Por fim, foi utilizada a biblioteca `pprint` para melhor exibição do dicionário obtido no terminal.  
Já para o acesso à câmera foi utilizada a função `PiCamera()` da biblioteca `picamera`. A função `sleep()`, da biblioteca `time` foi utilizada para se gerar os delays de tempo.

## API climática
A função `get` faz uma requisição HTTP de método GET para a URL fornecida como parâmetro. O retorno da função é a resposta da requisição. A requisição retorna diversas informações, como o código de resposta, etc, mas as informações que nos interessam estão contidas no corpo da resposta, que pode ser acessado como `.text`. Dessa forma, a função que executa a requisição ficou como

```py
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/966583'
stations_json = get(weather).text
```

Como dito anteriormente, a requisição retorna um objeto JavaScript. Sendo assim, o seguinte trecho de código mostra a conversão de objeto JS para dicionário PY.

```py
stations_dict = json.loads(stations_json)['items'][0]
```

Note que o objeto/dicionário é composto por uma única lista, `'items'`, que, por sua vez, é composta por um único objeto/dicionário. Assim, usou-se `['items']` para acessar a lista e `[0]` para acessar esse objeto, apenas para fins de simplificação do output.

Para display deste dicionário no terminal foi utilizada a função `pprint()`. Foi também usada a função `type()` para confirmação de que o objeto JS havia sido corretamente convertido em um dicionário PY. O resultado é apresentado a seguir

```
{'air_pressure': 1010.51,
 'air_quality': 48.8,
 'ambient_temp': 29.93,
 'created_by': 'UFSC',
 'created_on': '2018-09-27T16:10:21Z',
 'ground_temp': 23.06,
 'humidity': 46.42,
 'id': 13228613,
 'rainfall': 0,
 'reading_timestamp': '2018-09-27T16:10:21Z',
 'updated_by': 'UFSC',
 'updated_on': '2018-10-04T15:35:19.899Z',
 'weather_stn_id': 966583,
 'wind_direction': 90,
 'wind_gust_speed': 0,
 'wind_speed': 0}
<class 'dict'>
```

## Acesso à câmera

Primeiro, definiu-se a `camera` utilizando a função `PiCamera()` importada da biblioteca discutida anteriormente e configurou-se a resolução da câmera, como mostra o trecho a seguir:

```py
camera = PiCamera()
camera.resolution = (1024, 768)
```

O comando `start_preview()` inicia o preview da camera no monitor, como um *viewfinder*, podendo ser terminado com o comando `stop_preview()`.  
Para a primeira foto foi utilizado o trecho a seguir.

```py
camera.start_preview()
sleep(2)
camera.capture('sel0337.jpg')
camera.stop_preview()
```

Onde a função `sleep(2)` gera um delay de 2 segundos e a função `capture()` realiza uma captura (foto), salvando-a no endereço e formato especificados no parâmetro da função.

A adição do comando `annotate_text` pode ser utilizado antes da captura para se adicionar um trecho de texto à imagem salva, como mostra o trecho a seguir.

```py
camera.start_preview()
camera.annotate_text = "10748434 e 10788697"
sleep(5)
camera.capture('/home/sel/SEL0337/flavio_pimenta/pimenta_crush.jpg')
camera.stop_preview()
```

Por último, o comando `capture()` pode ser substituido pelo comando `start_recording()` para se iniciar uma captura de vídeo que, por sua vez, pode ser terminada com o comando `stop_recording()`. Semelhantemente à função `capture()`, a função `start_recording()` também recebe um parâmetro que indicia onde e em qual formato será salvo o arquivo de vídeo.

```py
camera.start_preview()
camera.annotate_text = "Vai BRASIL"
camera.start_recording('/home/sel/SEL0337/flavio_pimenta/hexa.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()
```

Todos os arquivos de foto e vídeo estão disponíveis no repositório desta prática no GitHub.