<style scoped>
	.dishes {
			margin-top: 1%;
			margin-bottom: 1%;
			margin-left: 5%;
			margin-right: 5%;
			width: 80%;
	}
	p {
		font-size: 20px;
		color: #80848f;
	}
	#buttongroup {
		margin-top: -50px;
		margin-right: 10px;
	}
	#photo-list {
		width: 80px;
		height: 80px;
		background-color: #bbbec4;
		margin-left: auto;
		margin-right: auto;
	}
</style>

<template>
	<Card :bordered="false" class="dishes" >
		<Row>
			<Col span="4">
				<div id="photo-list">
					<img :src="image" style="height:100%;width:100%;">
				</div>
			</Col>
			<Col span="8">
				<p>{{dishname}}</p>
				<p>{{description}}</p>
			</Col>
			<Col span="3">
				<p>价格：</p>
				<p>{{price}}</p>
			</Col>
			<Col span="3">
				<p>月销量：</p>
				<p>----------</p>
			</Col>

		</Row>
		<ButtonGroup style="float: right" id="buttongroup">
					<Button type="primary" v-on:click="modal1 = true">修改</Button>
					<Button v-on:click="$emit('remove')">删除</Button>
					<Modal width=700 v-model="modal1" @on-ok="ok" @on-cancel="cancel" :mask-closable="false" :closable="false">
						<h2 slot="header">添加菜品</h2>
						<Editwindow v-bind:srcdescription="this.description" 
									v-bind:srcdishname="this.dishname"
									v-bind:srcimage="this.image"
									v-bind:srcdishprice="this.price"
									v-on:UpdateDish="Refresh"
									ref="editwin"></Editwindow>
					</Modal>
					<Modal v-model="modal2">
						<Input></Input>
					</Modal>
				</ButtonGroup>
		<hr style="margin-top: 20px" />
		
		
	</Card>
</template>

<script>
	import Editwindow from '@/components/Editwindow'

	export default {
		data() {
			return {
				modal1: false,
				modal2: false,
				tempname: '',
				tempdescription: '',
				tempprice: '',
				tempimage: '',
				change: false
			}
		},
		methods: {
			ok() {

				if (this.change == true) {

					if (this.tempname=='') {
						this.$Modal.warning({
							title: '菜品名称不能为空',
							content: '请输入菜品名称'
						});
								
					} else if (this.tempdescription=='') {

						this.$Modal.warning({
							title: '菜品描述不能为空',
							content: '请输入菜品描述'
						});
								
					} else if (this.tempprice=='') {

						this.$Modal.warning({
							title: '菜品价格不能为空',
							content: '请输入菜品价格'
						});
								
					} else if (this.tempimage=='') {

						this.$Modal.warning({
							title: '菜品图片不能为空',
							content: '请上传菜品图片'
						});
								
					} else {
						this.$Modal.confirm({
						title:'确认修改',
						content:'确认对菜品信息进行修改？',
						loading:true,
						onOk: () => {
		
							var _this = this;
							this.axios.put('api/food/4/'+this.dishid, {
								food_name: _this.tempname,
								description: _this.tempdescription,
								price:_this.tempprice,
								image:_this.tempimage,
								priority:1
							})
							.then(function(response) {
								_this.$Modal.remove();
								_this.$Message.success('修改成功！');
								console.log(response);
								_this.dishname = _this.tempname;
								_this.description = _this.tempdescription;
								_this.price = _this.tempprice;
								_this.image = _this.tempimage;

							})
							.catch(function(error) {
								_this.$Modal.remove();
								_this.$Message.error('修改失败！');
								console.log(error);
							});
							
						}
						});
					}

					


					
					
				}
				this.change = false;
			},
			cancel() {
				this.$refs.editwin.reset()
			},
			Refresh(data) {
				this.tempname = data.EditedName;
				this.tempdescription = data.EditedDescription;
				this.tempprice = data.EditedPrice;
				this.tempimage = data.EditedImage
				this.change = true;
			}
		},
		props: ['dishname', 'description', 'price', 'dishid', 'image'],
		components: {
			Editwindow
		}
	}
</script>