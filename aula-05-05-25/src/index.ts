import Fastify from 'fastify'
const api = Fastify()

api.get('/', (req, res) => {
    return res.status(201).send({message: 'Hello World.'})
})

api.listen({port: 3000}, (err, address) => {
    if (err) {
        console.log('Erro na API')
        process.exit(1)
    } else {
        console.log(`Servidor iniciado em ${address}`)
    }
})