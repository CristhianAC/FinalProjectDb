import { defineConfig } from 'astro/config';
import tailwind from "@astrojs/tailwind";
import react from "@astrojs/react";
import cloudflare from '@astrojs/cloudflare';
import auth from "auth-astro";

// https://astro.build/config
export default defineConfig({
  output: 'server',
  integrations: [tailwind(), react(), auth()],
  adapter: cloudflare()
});