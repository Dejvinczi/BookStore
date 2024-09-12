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
RUN yarn install --frozen-lockfile


####################### BUILDER #############################
FROM base AS builder
# Set production environment
ENV NODE_ENV=production
# Set working directory
WORKDIR /app
# Copy node_modules from deps stage
COPY --from=deps /app/node_modules ./node_modules
# Copy app
COPY . .
# Build
RUN yarn build


######################## RUNNER ##############################
FROM base AS runner
# Set production environment
ENV NODE_ENV production
# Set working directory
WORKDIR /app
# Set correct permissions for nextjs user and don't run as root
RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs
RUN mkdir .next
RUN chown nextjs:nodejs .next
# Automatically leverage output traces to reduce image size
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static
COPY --from=builder --chown=nextjs:nodejs /app/public ./public
# Expose port
EXPOSE 3000
# Start server
CMD ["node", "server.js"]