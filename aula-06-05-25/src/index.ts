import Fastify from 'fastify'
const api = Fastify()

import { userRoutes } from './routes/users-routes'
api.register(userRoutes, { prefix: '/users' })

api.listen({ port: 3000 }, (err, address) => {
    if (err) {
        console.log('Erro na API')
        process.exit(1)
    } else {
        console.log(`Servidor iniciado em ${address}`)
    }
})