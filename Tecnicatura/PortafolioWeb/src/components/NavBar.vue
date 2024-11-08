<template>
    <nav>
     <div class="navbar">
       <div clas="navbar-menu">
         <ul>
            <a v-for="nav in navegacion" :key="nav.nombre" href="nav.enlace" class="nav-item"> {{ nav.nombre }}</a>
         </ul>
       </div>
     </div>
   </nav>
</template>

<script setup>
import { ref } from 'vue';
const navegacion = ref([
   {id:1, nombre: 'Eduacación', enlace:'#educacion'},
   {id:2, nombre: 'Experiencia', enlace:'#experiencia'},
   {id:3, nombre: 'Proyectos', enlace:'#proyectos'},
   {id:4, nombre: 'Habilidades', enlace:'#habilidades'}
])
</script>

<style scoped>
.navbar {
 background-color: var(--vt-c-indigo);
 color: #ffffff;
 padding: 0.5rem 1rem;
 align-items: center;
}
.navbar-item {
 color: #fff;
 text-decoration: none;
 margin-right: 2rem;
}
.navbar-menu {
 display: flex;
 justify-content: flex-end;
}
.navbar-list {
 list-style: none;
}

a {
 border: 1px solid;
 border-color: hsla(0, 0%, 0%, 0.2);
 border-radius:  5px;
 /*Elimina lo subrayado de los enlaces y elementos con clase "green*/
 text-decoration: none;
 /*Añade una trasición suave  para los cambios de estilo*/
 transition: 0.4s; 
 /* Añade padding alrededor del contenido*/
 padding: 5px;
}

a:hover {
 /*Cambia el color del fondo el mouse sobre un enlace*/
 background-color:  hsla(160, 100%, 37%, 0.2);
}

@media (max-width:768px) {
 .navbar-menu {
   display: flex;
   justify-content: flex-end;
   width: 100%;
 }
}
</style>