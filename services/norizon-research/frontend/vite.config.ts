import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		host: '0.0.0.0',
		port: 5173,
		proxy: {
			'/api': {
				target: process.env.DEEPRESEARCH_API_URL || 'http://localhost:5001',
				changeOrigin: true,
				rewrite: (path) => path.replace(/^\/api/, '')
			},
			// Proxy for audio files
			'/data': {
				target: process.env.DEEPGRAM_SERVICE_URL || 'http://nora-deepgram-dev:8002',
				changeOrigin: true
			}
		}
	}
});
