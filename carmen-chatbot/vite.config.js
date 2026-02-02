import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Plugin to replace process.env with browser-safe values
function browserCompat() {
  return {
    name: 'browser-compat',
    config() {
      return {
        define: {
          'process.env.NODE_ENV': JSON.stringify('production'),
          'global': 'globalThis'
        }
      }
    },
    resolveId(id) {
      if (id === 'process') {
        return { id: 'process-browser', external: false }
      }
    },
    load(id) {
      if (id === 'process-browser') {
        return {
          code: `export const env = {}; export default { env: {} };`,
          moduleSideEffects: false
        }
      }
    }
  }
}

export default defineConfig({
  plugins: [react(), browserCompat()],
  define: {
    'process.env.NODE_ENV': JSON.stringify('production'),
    'global': 'globalThis',
    __DEV__: 'false'
  },
  build: {
    lib: {
      entry: './src/main.tsx',
      name: 'CarmenChatbot',
      fileName: 'carmen-chatbot',
      formats: ['iife']
    },
    rollupOptions: {
      output: {
        // Inline CSS in JS for single file
        assetFileNames: 'carmen-chatbot.css'
      }
    },
    minify: 'terser',
    sourcemap: false,
    target: 'es2015'
  }
})
