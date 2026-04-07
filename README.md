# ocsnau-kiosk

## Recommended IDE Setup

[VS Code](https://code.visualstudio.com/) + [Vue (Official)](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Recommended Browser Setup

- Chromium-based browsers (Chrome, Edge, Brave, etc.):
  - [Vue.js devtools](https://chromewebstore.google.com/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd)
  - [Turn on Custom Object Formatter in Chrome DevTools](http://bit.ly/object-formatters)
- Firefox:
  - [Vue.js devtools](https://addons.mozilla.org/en-US/firefox/addon/vue-js-devtools/)
  - [Turn on Custom Object Formatter in Firefox DevTools](https://fxdx.dev/firefox-devtools-custom-object-formatters/)

## Type Support for `.vue` Imports in TS

TypeScript cannot handle type information for `.vue` imports by default, so we replace the `tsc` CLI with `vue-tsc` for type checking. In editors, we need [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) to make the TypeScript language service aware of `.vue` types.

## Customize configuration

See [Vite Configuration Reference](https://vite.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Type-Check, Compile and Minify for Production

```sh
npm run build
```
---

# ocsnau-kiosk

Цей шаблон має допомогти вам розпочати розробку з Vue 3 у Vite.

## Рекомендоване налаштування IDE

[VS Code](https://code.visualstudio.com/) + [Vue (Офіційний)](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (і вимкніть Vetur).

## Рекомендоване налаштування браузера

- Браузери на базі Chromium (Chrome, Edge, Brave тощо):
- [Vue.js devtools](https://chromewebstore.google.com/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd)
- [Увімкнути форматування власних об'єктів у Chrome DevTools](http://bit.ly/object-formatters)
- Firefox:
- [Vue.js devtools](https://addons.mozilla.org/en-US/firefox/addon/vue-js-devtools/)
- [Увімкнути форматування власних об'єктів у Firefox DevTools](https://fxdx.dev/firefox-devtools-custom-object-formatters/)

## Підтримка типів для імпорту `.vue` у TS

TypeScript за замовчуванням не може обробляти інформацію про тип для імпорту `.vue`, тому ми замінюємо CLI `tsc` на `vue-tsc` для перевірки типів. У редакторах нам потрібен [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar), щоб служба мови TypeScript знала про типи `.vue`.

## Налаштування конфігурації

Див. [Довідник з конфігурації Vite](https://vite.dev/config/).

## Налаштування проекту

```sh
npm install
```

### Компіляція та гаряче перезавантаження для розробки

```sh
npm run dev
```

### Перевірка типів, компіляція та мініфікація для продакшену

```sh
npm run build
```