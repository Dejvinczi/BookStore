/** @type {import('next').NextConfig} */
const nextConfig = {
  output: process.env.NODE_ENV === "production" ? "standalone" : undefined,

  // Defines of envs available on client side
  // env: {
  //   CUSTOM_ENV_VARIABLE: process.env.NODE_ENV === 'production'
  //     ? 'production_value'
  //     : 'development_value',
  // },

  images: {
    remotePatterns: [
      {
        protocol: process.env.NEXT_PUBLIC_API_PROTOCOL,
        hostname: process.env.NEXT_PUBLIC_API_HOST,
        port: process.env.NEXT_PUBLIC_API_PORT,
        pathname: "/media/**",
      },
    ],
  },

  // Function to modify webpack configuration - allows to customize the build process
  webpack: (config, { dev, isServer }) => {
    config.devtool = dev ? "eval-source-map" : "source-map";

    // Place for additional webpack config modifications
    if (!isServer) {
      // Modifications only for client-side code
    }

    return config;
  },

  // Additional Next.js configuration options
  // i18n: {
  //   locales: ['pl', 'en'],
  //   defaultLocale: 'en',
  // },
  poweredByHeader: false, // Disable "X-Powered-By: Next.js" header
};

export default nextConfig;
