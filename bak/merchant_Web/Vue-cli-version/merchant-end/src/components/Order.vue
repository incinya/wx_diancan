<template>
    <Content :style="{padding: '0 16px 16px'}">
        <Breadcrumb :style="{margin: '16px 0'}">
            <BreadcrumbItem>主页</BreadcrumbItem>
            <BreadcrumbItem>订单管理</BreadcrumbItem>
        </Breadcrumb>
        <div class="main-wrapper">
            <h1> 订单 </h1>
            <div class="table-wrapper">
                <Table stripe size="large" :columns="orderHeader" :data="orderItems"></Table>
                <h3 v-if="orderItems.length === 0">正在获取订单数据，请耐心等待...</h3>
            </div>
        </div>
    </Content>
</template>

<script>
    export default {
        data () {
            return {
                timeout: true,
                orderHeader: [
                    {
                        title: '订单编号',
                        key: 'order_id'
                    },
                    {
                        title: '桌号',
                        key: 'table_id'
                    },
                    {
                        title: '总价',
                        key: 'total_price'
                    },
                    {
                        title: '点餐时间',
                        key: 'order_time_format',
                        render: (h, params) => {
                            let date = new Date(params.row.order_time);
                            let formatDate = `
                                ${date.getFullYear()}-${date.getMonth().toString().padStart(2, '0')}-${date.getDate().toString().padStart(2, '0')} 
                                ${date.getHours().toString().padStart(2, '0')}:${date.getMinutes().toString().padStart(2, '0')}:${date.getSeconds().toString().padStart(2, '0')}
                            `
                            return h('span', formatDate)
                        }
                    },
                    {
                        title: '操作',
                        key: 'action',
                        render: (h, params) => {
                            return h('div', [
                                h('Button', {
                                    props: {
                                    type: 'primary',
                                    size: 'small'
                                    },
                                    style: {
                                    marginRight: '5px'
                                    },
                                    on: {
                                    click: () => {
                                        this.showDetailModal(params.index)
                                    }
                                    }
                                }, '查看')
                            ])
                        }
                    }
                ],
                orderItems: []
            }
        },
        methods: {
            showDetailModal (index) {
                this.$Modal.info({
                    width: '600px',
                    title: '订单内容',
                    render: (h) => {
                        return h('div', [
                            h('div', {
                                style: {
                                    padding: '12px 0',
                                    fontSize: '14px'
                                }
                            },
                            [
                                h('p', {
                                    style: {
                                        display: 'inline-block',
                                        padding: '0 12px'
                                    }
                                }, 
                                '订单号：' + this.orderItems[index].order_id),

                                h('p', {
                                    style: {
                                        display: 'inline-block',
                                        padding: '0 12px'
                                    }
                                }, 
                                 '桌号：' + this.orderItems[index].table_id),

                                h('p', {
                                    style: {
                                        display: 'inline-block',
                                        padding: '0 12px'
                                    }
                                }, 
                                 '总价：' + this.orderItems[index].total_price)    
                            ]),
                            h('Table', {
                                props: {
                                    size: 'default',
                                    columns: [{
                                        title: '菜名',
                                        key: 'food_name',
                                        render: (h, params) => {
                                            return h('span', params.row.food.food_name)
                                        }
                                    }, {
                                        title: '描述',
                                        key: 'description',
                                        render: (h, params) => {
                                            return h('span', params.row.food.description)
                                        }
                                    }, {
                                        title: '单价',
                                        key: 'price',
                                        render: (h, params) => {
                                            return h('span', params.row.food.price)
                                        }
                                    }, {
                                        title: '数量',
                                        key: 'num'
                                    }],
                                    data: this.orderItems[index].detail
                                },
                                on: {
                                    input: (val) => {
                                        this.value = val;
                                    }
                                }
                            })
                        ])
                    }
                })
            },
            updateData() {
                /* 蜜汁4号餐厅 */
                this.axios.get('/api/restaurant/orders/4')
                    .then(res => {
                        if(res.status =='200') {
                            console.log(res)
                            this.$set(this,'orderItems', res.data)
                        } else {
                            console.log("获取订单失败")
                        }
                        
                    })
                    .catch(err => {
                        console.log('err: ', err)
                        if(err.status == '400') {
                            console.log("获取订单失败")
                        }
                    });

                /* dangerous!! */
                if (this.timeout) 
                    setTimeout(this.updateData.bind(this), 10000);
            }
        },
        created() {
            console.log('order created');
            this.timeout = true;
            this.updateData();
        },
        destroyed() {
            this.timeout = false;
        }
        
    }
</script>

<style scoped>
    .main-wrapper {
        min-height: 500px;
        width: 100%;
        border: 1px solid #dddee1;
        border-color: #e9eaec;
        border-radius: 4px;
        padding: 24px;
        background: #fff;
        font-size: 14px;
        box-sizing: border-box;
    }
    
    .table-wrapper {
        margin-top: 24px;
    }
    
    .table-content {
        font-size: 20px;
    }
</style>