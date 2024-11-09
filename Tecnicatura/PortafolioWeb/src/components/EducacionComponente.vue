<template>
  <div class="timeline">
    <h2 class="timeline-title">¡Nuestra increíble línea del tiempo!</h2>
    <h3 class="timeline-subtitle">Nuestro viaje educativo: ¡cursos, desafíos y logros!</h3>
    <ul>
      <li v-for="(event, index) in events" :key="index" class="timeline-item">
        <!-- Línea central de la timeline -->
        <div class="timeline-line"></div>

        <!-- Contenido alternado a la izquierda o derecha -->
        <div :class="['timeline-content', index % 2 === 0 ? 'left' : 'right']">
          <div class="timeline-date">{{ event.date }}</div>
          <h3 class="event-title">{{ event.title }}</h3>
          <p class="event-description">{{ event.description }}</p>
        </div>

        <!-- Marcador de la timeline -->
        <div class="timeline-marker" :style="{ backgroundColor: event.color }"></div>
      </li>
    </ul>
  </div>
</template>

<script>
const Educacion = [
  { date: "2024", title: "Primer Semestre", description: "Comenzamos a estudiar en UTN FRRS en la tecnicatura en programación", color: "#4caf50" },
  { date: "2024", title: "Segundo Semestre", description: "Iniciamos el segundo semestre en la tecnicatura", color: "#2196f3" },
  { date: "2025", title: "Tercer Semestre", description: "Iniciamos el tercer semestre con nuevas materias en desarrollo web y aplicaciones móviles", color: "#3f51b5" },
  { date: "2025", title: "Cuarto Semestre", description: "Iniciamos el cuarto semestre con nuevas materias en desarrollo web y aplicaciones móviles", color: "#009688" },
  { date: "2025", title: "Graduación", description: "Finalizamos la tecnicatura y nos graduamos de la UTN", color: "#795548" }
];

export default {
  name: "TimelineEducacion",
  data() {
    return {
      events: Educacion,
    };
  },
};
</script>

<style scoped>
.timeline {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 40px;
  background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
  border-radius: 15px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  text-align: center;
  max-width: 1000px;
  margin: 30px auto;
}

.timeline-title {
  font-size: 2.8em;
  font-weight: 700;
  color: #333;
  margin-bottom: 10px;
  text-transform: uppercase;
  letter-spacing: 2px;
  background: -webkit-linear-gradient(45deg, #ff6b81, #ff9e3a);
  -webkit-background-clip: text;
  color: transparent;
  animation: fadeInText 2s ease-in-out;
}

.timeline-subtitle {
  font-size: 1.6em;
  color: #555;
  font-weight: 300;
  margin-bottom: 20px;
  opacity: 0;
  animation: fadeInSubtitle 2s 1s forwards;
}

.timeline-item {
  display: flex;
  position: relative;
  margin-bottom: 50px;
  justify-content: center;
  width: 100%;
}

.timeline-line {
  position: absolute;
  width: 4px;
  background-color: #ccc;
  top: 0;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  z-index: 1;
}

.timeline-marker {
  width: 35px;
  height: 35px;
  border-radius: 50%;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  z-index: 2;
  border: 3px solid #fff;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
  top: 0;
  transition: all 0.3s ease;
}

.timeline-content {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background-color: #000000;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  width: 280px;
  min-height: 160px;
  position: relative;
  text-align: center;
  margin-top: 15px;
  transition: all 0.3s ease;
}

.timeline-content.left {
  transform: translateX(-200px);
}

.timeline-content.right {
  transform: translateX(200px);
}

.timeline-content:hover {
  background-color: #333;
}

.timeline-item:hover .timeline-content {
  box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.2);
}

.timeline-item:hover .timeline-marker {
  transform: scale(1.2);
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
}

.timeline-date {
  font-weight: bold;
  color: #ff5722;
  font-size: 1.2em;
  padding-bottom: 10px;
  font-style: italic;
}

.event-title {
  font-size: 1.4em;
  color: #fff;
  margin: 0 0 15px;
  text-transform: capitalize;
  font-weight: bold;
}

.event-description {
  color: #c2c1c1;
  line-height: 1.6;
  flex-grow: 1;
}

/* Animaciones */
@keyframes fadeInText {
  from {
    opacity: 0;
    transform: translateY(-30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeInSubtitle {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

/* Estilos para pantallas pequeñas (móviles) */
@media (max-width: 768px) {
  .timeline-content {
    width: 100%;
    transform: translateX(0);
    text-align: center;
    margin-bottom: 20px;
  }

  .timeline-line {
    left: 0; /* Línea en el borde izquierdo */
  }

  .timeline-content.left,
  .timeline-content.right {
    transform: translateX(0);
  }
}
</style>
