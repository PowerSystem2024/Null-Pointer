<style scoped>
</style>

<script setup>
import linkedin from '/src/assets/linkedin_icon.svg';
import instagram from '/src/assets/instagram_icon.svg';
import github from '/src/assets/github_icon.svg';
import curriculum from '/src/assets/cv_resume_icon.svg';

const title = 'GRUPO NULL POINTER';
const descripcion = 'Técnicos Universitarios en Programación - UTN';
const residencia = 'San Rafael, Mendoza, Argentina';
const presentacion = 'Hola, Bienvenido a nuestro portafolio de proyectos. Somos estudiantes de desarrollado web y aplicaciones. Nuestra pasioqón es aprender sobre los diversos lenguajes de programación';
const redesSociales = [
  { id: 1, name: 'linkedin', src: linkedin , url: ''},
  { id: 2, name: 'Instagram', src: instagram , url: '' },
  { id: 3, name: 'github', src: github, url: 'https://github.com/PowerSystem2024/Null-Pointer' },
  { id: 4, name: 'curriculum', src: curriculum, url: '' },
];
const telefono = '2604-......';
</script>

<template>
  <section class="datos-personales">
    <div class="card">
      <h1>{{ title }}</h1>
      <h2>{{ descripcion }}</h2>
      <p>{{ presentacion }}</p>
      <ul class="container-lista">
        <li v-for="red in redesSociales" :key="red.id">
          <a :href="red.url"><img class="icon-redsocial" :src="red.src" width="35rem" :alt="red.name"></a>
        </li>
      </ul>
      <h3>☎ Nuestros Teléfono personal: {{ telefono }}</h3>
      <h4>{{ residencia }}</h4>
    </div>
  </section>
</template>

<style scoped>
h1 {
  font-size: 2.5rem;
}

p {
  font-size: 1.2rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.card {
  background-color: rgb(28, 41, 52);
  border-radius: 10px;
  padding: 10px;
  margin: 10px;
  text-align: center;
}

.container-lista {
  display: flex;
  justify-content: center;
  list-style: none;
  padding: 0;
  margin: 0;
  text-align: center;
}

.icon-redsocial {
  align-items: center;
  background-color: aliceblue;
  border-radius: 50%;
  padding: 2px;
  margin: 5px;
  box-shadow: 0 0 5px rgba(95, 124, 205, 0.934);
}

.icon-redsocial:hover {
  background-color: rgb(28, 41, 52);
  box-shadow: 0 0 5px rgba(251, 249, 249, 0.934);
}

h3 {
  font-size: 1.2rem;
  font-weight: 600;
}
</style>