<script setup>
import proyecto1 from "/src/assets/ahorcadopseint.jpg";
import proyecto2 from "/src/assets/ahorcado-imagen.jpg";
import { ref } from 'vue';
var misProyectos = ref([]);
misProyectos.value = ([
    {
        id: 1,
        src: proyecto1,
        titulo: "Ahorcado en pseint",
        description: "Con el grupo de la tecnicatura hicimos un juego llamado ahorcado en Pseint",
        projectoLink: "https://www.google.com.ar",
        githubLink: "https://www.github.com"
    },
    {
        id: 2,
        src: proyecto2,
        titulo: "Ahorcado en Java",
        description: "Con el grupo de la tecnicatura hicimos un juego llamado ahorcado en lenguaje de Java",
        projectoLink: "https://www.google.com.ar",
        githubLink: "https://www.github.com"
    },

])

</script>

<template>
    <div class="galeria">
        <li class="proyecto" v-for="proyecto in misProyectos" :key="proyecto.id">
            <img :src="proyecto.src" :alt="proyecto.titulo">
            <div class="proyecto-info">
                <h3>{{ proyecto.titulo }}</h3>
                <p>{{ proyecto.description }}</p>
                <div class="proyecto-links">
                    <a href="proyecto.proyectoLink" class="btn-ver-mas" target="_blank" rel="noopener noreferrer">Ver
                        Proyecto </a>
                    <a href="proyecto.githubLink" class="github-link" target="_blank" rel="noopener noreferrer"> Ver
                        Codigo en GitHub</a>
                </div>
            </div>
        </li>
    </div>
</template>

<style scoped>
/* .galeria{
    width: 100%;
    height: 100vh;
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center;
    background-image: url('/src/assets/foto-proyecto.jpg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
} */

.galeria {
    width: 100%;
    height: 100%;
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    padding: 20px;
    justify-content: center;
    background: linear-gradient(-70deg, #161616, #13571f, #089754,#00ff3798);
    background-size: 400% 400%;
    animation: gradient 10s ease infinite
}

@keyframes gradient {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }

}
.proyecto {
    display: flex;
    flex-direction: column;
    border: 2px solid #ddd;
    border-radius: 8px;
    overflow: hidden;
    background-color: #f9f9f9;
    max-width: 222px;
    flex: 1 1 300px;
}
.poyecto img {
    width: 100%;
    height: auto;
    display: block;
}
.proyecto-info{
    padding: 15px;
    text-align: center;
}
.proyecto-info h3 {
    margin: 10px 0;
    font-size: 1.3rem;
    color: #333;
}
.proyecto-info p {
    margin: 10px 0;
    font-size: 1em;
    color: #666;
}
.proyecto-links {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-top: 10px;
}
.proyecto-links .btn-ver-mas {
    background-color: #064700;
    color: #fff;
    padding: 10px 15px;
    border-radius: 5px;
    text-decoration: none;
    transition: background-color 0.3s;
}
.proyecto-links .btn-ver-mas:hover {
    background-color: #02b311;
}
.proyecto-links .github-link {
    color: #333;
    text-decoration: none;
    font-size: 0.9em;
}
.proyecto-links .github-link:hover {
    text-decoration: underline;
}
</style>