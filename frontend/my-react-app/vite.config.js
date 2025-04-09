import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': 'http://localhost:5000'
    },
  },
  // for production build
  build: {
    outDir: "../backend/static",
    emptyOutDir: true
  },
  test: {
    globals: true,
    environment: 'jsdom'
  }
});
