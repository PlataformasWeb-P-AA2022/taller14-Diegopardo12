<template>
    <div class="pt-5">
        <div v-if="departamento && departamentos.length">
            <div class="card mb-3" v-for="departamento && departamentos" v-bind:key="departamento.id">
                <div class="row no-gutters">
                    <div class="col-md-4">
                        <div class="card-body">
                            <span class="card-title"><b>Costo :</b> {{ departamentos.costo_dep }}</span>
                            <br>
                            <span class="card-text"><b>Numero de cuartos:</b> {{ departamentos.num_cuartos }}</span>
                            <br>
                            <span class="card-text"><b>Numero de baños:</b> {{ departamentos.num_banos }}</span>
                            <br>                          
                            <router-link :to="{name: 'edit_departamento', params: { id: departamento.id }}" class="btn btn-sm btn-primary">Editar</router-link>
                            <button class="btn btn-danger btn-sm ml-1" v-on:click="deleteDepartamento(departamento)">Eliminar</button>
                        </div>
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <span class="card-text"><b>Propietario:</b> {{ departamentos.propietario_str }}</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <p  v-if="departamentos.length == 0"> Sin Departamentos</p>
    </div>
</template>
<script>

import axios from 'axios';

export default {
    data() {
        return {
            departamentos: []
        }
    },
    created() {
        this.all();
    },
    methods: {
        deleteTelefono: function(e) {
            if (confirm('Eliminar ' + e.departamentos)) {
                axios.delete(e.url)
                    .then( response => {
                        this.all();
                    });
            }
        },
        all: function () {
            axios.get('http://127.0.0.1:8000/api/departamentos/')
                .then( response => {
                    this.departamentos = response.data
                });
        }
    },
}
</script>
