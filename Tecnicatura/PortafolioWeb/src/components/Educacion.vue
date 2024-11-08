<template>
    <div class="timeline">
      <h2>Nuestra linea del Tiempo</h2>
      <ul>
        <li v-for="(event, index) in events" :key="index" class="timeline-item">
          <div class="timeline-marker" :style="{ backgroundColor: event.color }"></div>
          <div v-if="index < events.length - 1" class="timeline-line"></div>
          <div class="timeline-content">
            <div class="timeline-date">{{ event.date }}</div>
            <h3>{{ event.title }}</h3>
            <p>{{ event.description }}</p>
          </div>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  // Definimos los eventos como una constante fuera del objeto Vue
  const Educacion = [
    { date: "2024", title: "Primer Semestre", description: "Comenzamos a estudiar en UTN Frsr en la tecnicatura en programacion", color: "#4caf50" },
    { date: "2024", title: "Segundo Semestre", description: "Comenzamos el segundo semestre en la tecnicatura", color: "#2196f3" },
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
    padding: 20px;
    max-width: 600px;
    margin: auto;
    position: relative;
  }
  .timeline h2 {
    text-align: center;
    margin-bottom: 20px;
  }
  .timeline-item {
    display: flex;
    align-items: flex-start;
    position: relative;
    margin-left: 30px;
    margin-bottom: 40px;
  }
  .timeline-marker {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    position: absolute;
    left: -30px;
    z-index: 2;
  }
  .timeline-line {
    position: absolute;
    width: 4px;
    background-color: #ccc;
    top: 20px;
    bottom: -40px;
    left: -20px;
    z-index: 1;
  }
  .timeline-content {
    background-color: #000000;
    border-radius: 8px;
    padding: 15px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    margin-left: 20px;
    max-width: 500px;
  }
  .timeline-date {
    font-weight: bold;
    color: #a5a5a5;
    padding-bottom: 5px;
  }
  .timeline-content h3 {
    margin: 0;
    font-size: 1.2em;
  }
  .timeline-content p {
    margin: 5px 0 0;
    color: #c2c1c1;
  }
  </style>