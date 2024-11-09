<script setup>
import icono1 from '/src/assets/ventas.svg';
import icono2 from '/src/assets/ecomerce.svg';
import icono3 from '/src/assets/configuracion.svg';
import icono4 from '/src/assets/uiux.svg';
import icono5 from '/src/assets/watch.svg';

import { ref } from 'vue';

const titulo = 'Experiencia como Desarrollador Full Stack';
const fecha = 'Enero 2022 - Julio 2024';
const experiencias = ref([
    { id: 1, src: icono1, parrafo: 'Lideramos el desarrollo de una plataforma de e-commerce que impulsó el crecimiento de las ventas en un 40% durante el primer año.' },
    { id: 2, src: icono2, parrafo: 'Optimizamos el rendimiento de sistemas web utilizando Node.js y React, lo que resultó en una reducción del tiempo de carga en un 60%.' },
    { id: 3, src: icono3, parrafo: 'Implementamos medidas avanzadas de seguridad que redujeron los intentos de acceso no autorizado en un 25% y mejoraron la integridad de los datos.' },
    { id: 4, src: icono4, parrafo: 'Colaboramos en el diseño de interfaces de usuario junto con el equipo de UX/UI, logrando un incremento en la retención de usuarios de un 20%.' },
    { id: 5, src: icono5, parrafo: 'Automatizamos procesos de despliegue mediante la integración de Jenkins y Docker, logrando una mejora del 45% en la eficiencia de los lanzamientos.' },
    { id: 6, src: icono5, parrafo: 'Desarrollamos sistemas de monitoreo y alertas que permitieron reducir en un 30% los tiempos de respuesta ante incidentes críticos.' }
]);

</script>

<template>
    <div class="contenedor">
        <h3 class="titulo">{{ titulo }}</h3>
        <p class="fecha">{{ fecha }}</p>
        <div class="tarjetas">
            <div class="tarjeta" v-for="experiencia in experiencias" :key="experiencia.id">
                <img class="icono" :src="experiencia.src" alt="Icono de experiencia" />
                <p class="descripcion">{{ experiencia.parrafo }}</p>
            </div>
        </div>
    </div>
</template>

<style scoped>
/* Fondo claro para el contenedor */
.contenedor {
    max-width: 800px;
    margin: 2rem auto;
    padding: 1.5rem;
    background-color: #f0f4ff;
    border-radius: 15px;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
    text-align: center;
}

/* Color principal vibrante y sombras para el título */
.titulo {
    font-size: 1.8rem;
    font-weight: 700;
    color: #4a6fa5;
    margin-bottom: 0.5rem;
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.1);
}

/* Color pastel para la fecha */
.fecha {
    font-size: 1rem;
    color: #7b8da0;
    margin-bottom: 2rem;
}

/* Diseño de cuadrícula y espaciado de las tarjetas */
.tarjetas {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
}

/* Tarjetas con colores gradientes y efectos suaves */
.tarjeta {
    background: linear-gradient(135deg, #ffffff, #e0eafc);
    border-radius: 10px;
    padding: 1.5rem;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    text-align: left;
    border: 1px solid #dde5f0;
}

/* Efecto hover colorido */
.tarjeta:hover {
    transform: translateY(-8px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
    border-color: #4a6fa5;
}

/* Iconos con un estilo suave y color gris */
.icono {
    width: 40px;
    height: 40px;
    margin-bottom: 1rem;
    filter: drop-shadow(1px 1px 2px rgba(0, 0, 0, 0.15));
}

/* Descripción con mejor legibilidad y un toque de color */
.descripcion {
    font-size: 0.95rem;
    color: #555;
    line-height: 1.4;
    font-weight: 500;
}
</style>
