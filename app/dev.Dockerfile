########################### BASE #################################
FROM node:20.14-alpine AS base


####################### DEPENDENCIES #############################
FROM base AS deps
# Set working directory
WORKDIR /app
# https://github.com/nodejs/docker-node/tree/b4117f9333da4138b03a546ec926ef50a31506c3#nodealpine
RUN apk add --no-cache libc6-compat
# Copy package.json file
COPY package.json ./package.json
# Install dependencies
RUN yarn install


####################### RUNNER ##############################
FROM base AS runner
# Set development environment
ENV NODE_ENV development
# Set working directory
WORKDIR /app
# Copy dependencies from deps stage
COPY --from=deps /app/node_modules ./node_modules
# Copy app
COPY . .
# Expose port
EXPOSE 3000
# Start server
CMD [ "yarn", "dev" ]