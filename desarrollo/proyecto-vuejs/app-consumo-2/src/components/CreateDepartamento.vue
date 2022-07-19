<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
            <div class="form-group">
                <label for="costo_dep">Costo Departamento</label>
                <input
                    type="number"
                    class="form-control"
                    id="costo_dep"
                    v-model="departamentos.costo_dep"
                    v-validate="'required'"
                    name="costo_dep"
                    placeholder="Ingrese costo del deparatamento"
                    :class="{'is-invalid': errors.has('departamentos.costo_dep') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid costo Departamento.
                </div>
            </div>

            <div class="form-group">
                <label for="num_cuartos">Numero de cuartos</label>
                <input
                    type="number"
                    class="form-control"
                    id="num_cuartos"
                    v-model="departamentos.num_cuartos"
                    v-validate="'required'"
                    name="num_cuartos"
                    placeholder="Ingrese el numero de cuartos"
                    :class="{'is-invalid': errors.has('departamentos.num_cuartos') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid numero de cuartos.
                </div>
            </div>

            <div class="form-group">
                <label for="num_banos">Numero de baños</label>
                <input
                    type="number"
                    class="form-control"
                    id="num_banos"
                    v-model="departamentos.num_banos"
                    v-validate="'required'"
                    name="num_banos"
                    placeholder="Ingrese el numero de baños"
                    :class="{'is-invalid': errors.has('departamentos.num_banos') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid numero de baños.
                </div>
            </div>


            <div class="form-group">
                <label for="valor_ali">Valor alicuota</label>
                <input
                    type="number"
                    class="form-control"
                    id="valor_ali"
                    v-model="departamentos.valor_ali"
                    v-validate="'required'"
                    name="valor_ali"
                    placeholder="Ingrese el valor de la alicuota"
                    :class="{'is-invalid': errors.has('departamentos.valor_ali') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid valor de la alicuota"
                </div>
            </div>


            <div class="form-group">
              <br>
                <label for="propietario">Propietario</label>
                <select v-model="departamentos.propietario">
                            <option v-for="e in propietarioList" :key="e.url" :value="e.url">{{ e.nombre }} {{ e.apellido }} {{e.edad}} {{e.nacionalidad}}</option>
                        </select>
            </div>
            <br>
            <button type="submit" class="btn btn-primary">Crear</button>
        </form>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    data() {
        return {
            departamentos: {
                costo_dep: '',
                num_cuartos: '',
                num_banos: '',
                valor_ali: '',
            },
            estudiantesList: [],
            submitted: false
        }
    },
    mounted() {
        this.getpropietarioList()
    },
    methods: {
      getpropietarioList() {
            axios
            .get('http://127.0.0.1:8000/api/propietario/')
            .then(response => {
                this.propietarioList = response.data
            })
            .catch(error => {
                console.log(error)
            })

        },
        create: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios.post('http://127.0.0.1:8000/api/departamentos/',
                        this.telefono
                    )
                    .then(response => {
                        this.$router.push('/telefonos');
                    })
            });
        }
    },
}
</script>
