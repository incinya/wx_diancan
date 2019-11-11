Vue.component('dish', {
    template:'<Card :bordered="false" class="dishes">\
                <p slot="title">{{dishname}}</p>\
                        <p>{{description}}</p><br></br>\
                        <i-button v-on:click="$emit(\'remove\')">delete</i-button>\
                    </Card>',
    props: ['dishname', 'description']
})



new Vue({
    	el:'#left-menu'
    })

new Vue({
    	el:'#top-menu'
    })

new Vue({
    	el:'#dishes',
        data: {
            newname: '',
            newdes: '',
            dishes: [
                {
                    id:1,
                    name:'dish1',
                    des:'description1',
                },
                {
                    id:2,
                    name:'dish2',
                    des:'description2',
                },
                {
                    id:3,
                    name:'dish3',
                    des:'description3'
                }
            ] ,
            newid: 4
        },
            methods: {
                addnewdish: function () {
                    this.dishes.push({
                        id: this.newid++,
                        name: this.newname,
                        des: this.newdes
                    })
                    this.newname = '';
                    this.newdes = '';
                }
            }
})

new Vue({
    	el:'#pages'
})

