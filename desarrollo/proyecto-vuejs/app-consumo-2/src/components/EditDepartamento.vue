<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
            <div class="form-group">
                <label for="deparatamentos">Costo Departamento</label>
                <input
                    type="text"
                    class="form-control"
                    id="costo_dep"
                    v-model=departamento.costo_dep"
                    v-validate="'required'"
                    name="costo_dep"
                    placeholder="Ingres costo del departamento"
                    :class="{'is-invalid': errors.has('departamento.costo_dep') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid name.
                </div>
            </div>

            <div class="form-group">
                <label for="num_cuartos">Numero de cuartos</label>
                <input
                    type="number"
                    class="form-control"
                    id="num_cuartos"
                    v-model="departamento.num_cuartos"
                    v-validate="'required'"
                    name="num_cuartos"
                    placeholder="Ingrese el numero de cuartos"
                    :class="{'is-invalid': errors.has('departamento.num_cuartos') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid numero cuartos.
                </div>
            </div>

            <div class="form-group">
                <label for="num_banos">Numero de baños</label>
                <input
                    type="number"
                    class="form-control"
                    id="num_banos"
                    v-model="departamento.num_banos"
                    v-validate="'required'"
                    name="num_banos"
                    placeholder="Ingrese el numero de baños"
                    :class="{'is-invalid': errors.has('departamento.num_banos') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid numero baños.
                </div>
            </div>

            <div class="form-group">
                <label for="valor_ali">Valor de alicuota</label>
                <input
                    type="number"
                    class="form-control"
                    id="valor_ali"
                    v-model="departamento.valor_ali"
                    v-validate="'required'"
                    name="valor_ali"
                    placeholder="Ingrese el valor de la alicuota"
                    :class="{'is-invalid': errors.has('departamento.valor_ali') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid alicuota.
                </div>
            </div>
            <div class="form-group">
              <br>
                <label for="propietario">Propietario</label>
                <select v-model="departamento.propietario">
                            <option v-for="e in propietarioList" :key="e.url" :value="e.url">{{ e.nombre }} {{ e.apellido }}</option>
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
            departamento: {
                costo_dep: '',
                num_cuartos: '',
                num_banos: '',
                valor_ali: '',
                propietario: '',
            },
            propietarioList: [],
            submitted: false
        }
    },
    mounted() {
        this.getpropietarioList(),
        axios.get('http://127.0.0.1:8000/api/deparatamentos/' + this.$route.params.id + '/')
            .then( response => {
                console.log(response.data)
                this.departamento = response.data
        });
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
                axios.put(`http://127.0.0.1:8000/api/deparatamentos/${this.deparatamentos.id}/`,
                        this.deparatamentos
                    )
                    .then(response => {
                        this.$router.push('/deparatamentos');
                    })
            });
        }
    },
}
</script>
