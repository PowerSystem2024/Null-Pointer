<script setup>
import img1 from '/src/components/icons/js.svg';
import img2 from '/src/components/icons/python.svg';
import img3 from '/src/components/icons/html-css.svg';
import img4 from '/src/components/icons/java.svg';
import img5 from '/src/components/icons/sql.svg';
import img6 from '/src/components/icons/react.svg';
import img7 from '/src/components/icons/vue.svg';
import img8 from '/src/components/icons/node.svg';
import img9 from '/src/components/icons/django.svg';
import img10 from '/src/components/icons/bootstrap.svg';
import img11 from '/src/components/icons/git.svg';
import img12 from '/src/components/icons/docker.svg';
import img13 from '/src/components/icons/cypress.svg';
import img14 from '/src/components/icons/figma.svg';
import img15 from '/src/components/icons/visual.svg';
import img16 from '/src/components/icons/mongo.svg';
import img17 from '/src/components/icons/mysql.svg';
import img18 from '/src/components/icons/postgres.svg';
import img19 from '/src/components/icons/arg.svg';
import img20 from '/src/components/icons/eeuu.svg';

// Se importa ref de vue para poder usarlo
import { ref } from 'vue';

// Se crea un array de objetos con las habilidades
const habilidades = ref([
    {
        id: 1, nombre: 'Lenguajes de Programación', habilidades: [
            { id: 1, nombre: 'JavaScript', nivel: 'Avanzado', icono: img1 },
            { id: 2, nombre: 'Python', nivel: 'Intermedio', icono: img2 },
            { id: 3, nombre: 'HTML/CSS', nivel: 'Avanzado', icono: img3 },
            { id: 4, nombre: 'Java', nivel: 'Intermedio', icono: img4 },
            { id: 5, nombre: 'SQL', nivel: 'Intermedio', icono: img5 }
        ]
    },
    {
        id: 2, nombre: 'Frameworks y Librerías', habilidades: [
            { id: 1, nombre: 'React.js', nivel: 'Avanzado', icono: img6 },
            { id: 2, nombre: 'Vue.js', nivel: 'Intermedio', icono: img7 },
            { id: 3, nombre: 'Node.js', nivel: 'Avanzado', icono: img8 },
            { id: 4, nombre: 'Django', nivel: 'Intermedio', icono: img9 },
            { id: 5, nombre: 'Bootstrap', nivel: 'Avanzado', icono: img10 }
        ]
    },
    {
        id: 3, nombre: 'Herramientas y Software', habilidades: [
            { id: 1, nombre: 'Git', nivel: 'Avanzado', icono: img11 },
            { id: 2, nombre: 'Docker', nivel: 'Intermedio', icono: img12 },
            { id: 3, nombre: 'Cypress', nivel: 'Intermedio', icono: img13 },
            { id: 4, nombre: 'Figma', nivel: 'Intermedio', icono: img14 },
            { id: 5, nombre: 'Visual Studio Code', nivel: 'Avanzado', icono: img15 }
        ]
    },
    {
        id: 4, nombre: 'Bases de Datos', habilidades: [
            { id: 1, nombre: 'MongoDB', nivel: 'Avanzado', icono: img16 },
            { id: 2, nombre: 'MySQL', nivel: 'Intermedio', icono: img17 },
            { id: 3, nombre: 'PostgreSQL', nivel: 'Intermedio', icono: img18 }
        ]
    },
    {
        id: 5, nombre: 'Idiomas', habilidades: [
            { id: 1, nombre: 'Español', nivel: 'Nativo', icono: img19 },
            { id: 2, nombre: 'Inglés', nivel: 'Avanzado (C1)', icono: img20 }
        ]
    }
]);

</script>

<template>
    <div class="skills-contenedor">
        <div v-for="habilidad in habilidades" :key="habilidad.id" class="skills-categoria">
            <h3>{{ habilidad.nombre }}</h3>
            <ul class="skills">
                <li v-for="habilidad in habilidad.habilidades" :key="habilidad.id" class="skill">
                    <img :src="habilidad.icono" :alt="habilidad.nombre">
                    <span>{{ habilidad.nombre }}: {{ habilidad.nivel }}</span>
                </li>
            </ul>
        </div>
    </div>
</template>

<style scoped>
.skills-contenedor {
    padding: 3rem;
    background: linear-gradient(-45deg, #52b857, #363b52, #226141, #241b0c);
    background-size: 400% 400%;
    animation: gradient-animation 10s ease infinite;
}

.skills-categoria {
    margin-bottom: 30px;
    padding: 1rem;
    border-radius: 10px;
    background-color: rgba(255, 255, 255, 0.1);
    box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.3);
}

.skills-categoria h3 {
    text-align: center;
    font-size: 1.8em;
    color: white;
    font-weight: 700;
    text-transform: uppercase;
    margin-bottom: 15px;
}

.skills {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    gap: 20px;
}

.skill {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 15px;
    background-color: rgba(0, 0, 0, 0.7);
    padding: 10px;
    border-radius: 15px;
    box-shadow: 0px 5px 15px rgba(0, 151, 151, 0.7);
    flex: 1 1 220px;
    max-width: 250px;
    transition: transform 0.3s ease, background-color 0.3s ease, box-shadow 0.3s ease;
}

.skill:hover {
    background-color: rgba(0, 151, 151, 0.9);
    transform: scale(1.05);
    box-shadow: 0px 10px 30px rgba(0, 151, 151, 0.9);
}

.skill img {
    width: 40px;
    height: 40px;
    transition: transform 0.3s ease;
}

.skill img:hover {
    transform: rotate(360deg);
}

.skill span {
    font-size: 1.1em;
    color: white;
    font-weight: 500;
}

@keyframes gradient-animation {
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

@media (max-width: 768px) {
    .skills-categoria h3 {
        font-size: 1.5em;
    }

    .skill {
        max-width: 100%;
        margin-bottom: 15px;
    }
}
</style>
