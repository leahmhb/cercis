<template>
    <div class="single-dog">
        <b-link :to="{name: 'poodle-detail', params: {slug:  poodle.slug }}" class="d-block">
            <span class="d-block float-right">
                <i :class="['d-inline', 'float-right', 'fas', iconClass]" :title="poodle.sex"></i>
                <span v-if="poodle.origin_country.code != 'UNK'" class="badge badge-light">{{ poodle.origin_country.code
                    }}</span>
                <span v-if="poodle.color" class="badge badge-light">{{ poodle.color.text }}</span>
            </span>
            {{ poodle.name_registered }}
        </b-link>
    </div>
</template>

<script>
    export default {
        name: 'SingleDog',
        props: [
            'poodle',
        ],
        computed: {
            iconClass: function () {
                var s = this.poodle.sex
                if (s == 'F') {
                    return 'fa-venus text-female';
                } else if (s == 'M') {
                    return 'fa-mars text-male';
                } else {
                    return 'fa-genderless text-light';
                }
            }
        },
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
   
</style>