// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  app: {
    head: {
      title: 'Kafka Tester',
      charset: 'utf-8',
      viewport: 'width=device-width, initial-scale=1',
    }
  },
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  modules: ['usebootstrap'],
  css: ["bootstrap/dist/css/bootstrap.min.css"],
  security: {
    headers: {
      crossOriginResourcePolicy: 'cross-origin',
    },
  },
  runtimeConfig: {
    public: {
      apiBase: 'http://locahost:5000/api',
    },
  },
})
