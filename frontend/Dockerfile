FROM node:22.11

COPY server/ /usr/app/server/
COPY plugins/ /usr/app/plugins/
WORKDIR /usr/app/
COPY package.json package-lock.json nuxt.config.ts tsconfig.json app.vue /usr/app/
RUN npm config set strict-ssl false && npm install

ENTRYPOINT ["npm", "run", "dev"]