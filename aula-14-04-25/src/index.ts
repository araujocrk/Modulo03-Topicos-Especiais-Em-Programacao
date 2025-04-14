import { fastify } from "fastify"

const server = fastify()

server.get('/', (req, res) => {
    return res.status(200).send({ message: 'Hello World' })
})

server.listen({ port: 3000 }, (err, adress) => {
    if (err) {
        console.error(err.message)
        process.exit(1)
    } 

    console.log(`Server started at ${adress}...`)
} )