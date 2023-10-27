import {defineConfig} from 'vite'
import react from '@vitejs/plugin-react-swc'
import {resolve} from 'path'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [react()],
    root: './src',

    server: {
        open: "src/overview/overview.html"
    },

    build: {
        rollupOptions: {
            input: {
                overview: resolve(__dirname, './src/character_sheet/html/overview.html'),
                character_sheet: resolve(__dirname, './src/character_sheet/html/detail.html')
            },
            output: {

            }
        },


        outDir: resolve(__dirname, "../backend/static"),


    }
})
