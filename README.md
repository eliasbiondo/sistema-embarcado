# Implementação de um Sistema de Comunicação Entre Computador e Sistema Embarcado

## Autores
Elias Biondo e Giovana Thomé  
Instituto de Tecnologia e Liderança

![Sistema](./public/preview.png)

## Resumo
O presente estudo foca na implementação de um sistema de comunicação entre um computador e o sistema embarcado Raspberry Pi Pico W, utilizando a linguagem de programação MicroPython. O Raspberry Pi Pico W, uma evolução do microcontrolador Raspberry Pi Pico, destaca-se por sua conectividade Wi-Fi, ampliando as possibilidades de uso em aplicações diversas. A aplicação desenvolvida visa medir a intensidade da luz, relevante tanto para automação residencial quanto industrial. A implementação envolveu o uso de resistores, LEDs, um sensor LDR e a programação em MicroPython para a coleta e exibição de dados de luminosidade. Os resultados obtidos em um ambiente controlado foram satisfatórios, e um exemplo prático do sistema operacional pode ser visualizado através de um vídeo disponibilizado online. O projeto evidencia o equilíbrio entre simplicidade e funcionalidade proporcionado pelo MicroPython, ressaltando o potencial de expansão e integração do sistema desenvolvido com outras plataformas e dispositivos.

Palavras-chave: sistema embarcado, Raspberry Pi Pico W, MicroPython, automação, medição de luz, comunicação computador-sistema.

## Vídeo demonstrativo
Para visualizar o exemplo prático da aplicação em funcionamento, acesse o vídeo no seguinte link: [Vídeo Demonstrativo](https://youtu.be/O3IyKL1WRJY).

## Referências
[1] RASPBERRY PI FOUNDATION. Raspberry Pi Pico: Documentation. Raspberry Pi Foundation, [s.d.]. Disponível em: [https://bit.ly/46VPAYe](https://bit.ly/46VPAYe). Acesso em: 17 nov. 2023.

## Estrutura de Pastas
```
.
├── README.md
├── app
│   ├── favicon.ico
│   ├── globals.css
│   ├── layout.tsx
│   └── page.tsx
├── next-env.d.ts
├── next.config.js
├── package-lock.json
├── package.json
├── postcss.config.js
├── public
│   ├── bulb-0.svg
│   └── bulb-1.svg
├── python
│   ├── main.py
│   └── simple.py
├── tailwind.config.ts
└── tsconfig.json
```

A estrutura de pastas do projeto é organizada da seguinte maneira:

- `.`: Raiz do projeto.
  - `README.md`: Arquivo Markdown contendo a documentação e descrição do projeto.
  - `app`: Diretório contendo os arquivos específicos da aplicação frontend.
    - `favicon.ico`: Ícone de favorito, mostrado nas abas do navegador.
    - `globals.css`: Arquivo CSS contendo estilos globais aplicáveis a toda a aplicação.
    - `layout.tsx`: Componente React para o layout da aplicação, possivelmente incluindo cabeçalho, rodapé, e outros elementos comuns.
    - `page.tsx`: Componente React representando uma página da aplicação.
  - `next-env.d.ts`: Arquivo de declaração de tipos para o Next.js, utilizado pelo TypeScript.
  - `next.config.js`: Arquivo de configuração do Next.js, onde é possível definir configurações personalizadas para o framework.
  - `package-lock.json`: Arquivo gerado automaticamente para qualquer operação que modifique o `node_modules` ou o `package.json`.
  - `package.json`: Arquivo contendo as dependências do projeto e scripts de execução.
  - `postcss.config.js`: Arquivo de configuração para o PostCSS, uma ferramenta de software que usa plugins JavaScript para transformar estilos CSS.
  - `public`: Diretório contendo arquivos estáticos acessíveis publicamente.
    - `bulb-0.svg`: Imagem em formato SVG representando uma lâmpada desligada.
    - `bulb-1.svg`: Imagem em formato SVG representando uma lâmpada ligada.
  - `python`: Diretório contendo os scripts em Python para o sistema embarcado.
    - `main.py`: Script principal em Python para a execução no Raspberry Pi Pico W.
    - `simple.py`: Script auxiliar em Python, possivelmente contendo funções simplificadas ou auxiliares.
  - `tailwind.config.ts`: Arquivo de configuração do Tailwind CSS, um framework de CSS utilitário.
  - `tsconfig.json`: Arquivo de configuração do TypeScript, definindo opções para o compilador de TypeScript.