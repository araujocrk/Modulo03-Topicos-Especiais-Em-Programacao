import { FastifyInstance } from "fastify"

export async function userRoutes(fastify:FastifyInstance) {
    
fastify.get('/', (req, res) => { // http://localhost:3000/<recurso plural>/<ação>/<param>
    return res.status(201).send(
        {
            message: 'Hello World.'
        })
})

fastify.get('/health', (req, res) => {
    return {
                message: 'ok'
           }
})

fastify.get('/list', (req, res) => {
    // Operação de consulta ao BD.
    return [
        {
            name: 'Zé'
        },
        {
            name: 'João'
        }
    ]
})    
}
