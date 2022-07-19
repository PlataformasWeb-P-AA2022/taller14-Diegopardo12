<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <h2><router-link to="/index">Administración de Departamentos</router-link></h2>
        <router-link to="/create_departamento" class="btn btn-sm btn-primary"> Agregar Departamento</router-link>
        <br>
        <router-link to="/telefonos" class="btn btn-sm btn-primary">Ver Departamentos</router-link>
        <br>
        <router-link to="/create" class="btn btn-sm btn-primary">Agregar Propietario</router-link>

        <router-view />
      </div>
    </div>
  </div>
</template>
