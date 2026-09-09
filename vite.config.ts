import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
  ],
  base: '/kiosk/', // Важливо: додає префікс до всіх шляхів
  server: {
    proxy: {
      '/api-ocsnau': {
        target: 'https://ocsnau.net',
        changeOrigin: true,
        secure: false,
        rewrite: (path) => path.replace(/^\/api-ocsnau/, ''),
      },
    },
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
})
