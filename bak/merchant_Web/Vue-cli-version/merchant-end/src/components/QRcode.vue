<style scoped>
	#qrcode {
		margin-left: auto;
		margin-right: auto;
		width: 20%;
	}
	#tableid {
		margin-left: auto;
		margin-right: auto;
		margin-top: 5%;
		width: 17%;
	}
	#notice {
		margin-left: 36%;
		margin-right: auto;
		width: 50%;
	}
	#input {
		margin-left: 43%;
		margin-right: auto;
	}

</style>


<template>
	<Content :style="{padding: '0 16px 16px'}">
  	<Breadcrumb :style="{margin: '16px 0'}">
    	<BreadcrumbItem>主页</BreadcrumbItem>
    	<BreadcrumbItem>定制餐桌二维码</BreadcrumbItem>
    </Breadcrumb>
  	<Card>
      <div style="height: 1000px">
      	<h2 style="color: #80848f">定制餐桌二维码</h2>
      	<h2 id="tableid">餐桌编号：{{result}}</h2>
      	<br></br>
      	<div id="qrcode"></div>
      	<br></br>
      	<h3 style="color: #9ea7b4" id="notice">输入餐桌编号，点击确定即可生成相应二维码</h3>
      	<br></br>
		<InputNumber :min="1" v-model="tableid" id="input"></InputNumber>
		<Button type="ghost" shape="circle" v-on:click="generate_qrcode">确定</Button>
      </div>
  	</Card>
  </Content>

	

</template>

<script>
	import QRCode from 'qrcodejs2'
	export default {
		data() {
			return {
				tableid:1,
				qrcode:'',
				result:1,
			}
		},
		methods: {
			UpdateCode() {
				var obj = {
					restaurantId:4,
					tableId:this.tableid
				};

				this.qrcode.makeCode(JSON.stringify(obj));
					
				
				
				console.log(qrcode);
			},
			generate_qrcode() {
				
				this.UpdateCode();
				this.result=this.tableid;
				this.$Message.config({
					duration: 2
				});
				this.$Message.success('生成二维码成功，餐桌编号为'+this.result);
				this.tableid='';

			}
		},
		mounted() {
			var obj = {
				restaurantId:4,
				tableId:1
			};

			this.qrcode = new QRCode('qrcode', {
				width:200,
				height:200,
				text:JSON.stringify(obj)
			});
		}
	}
</script>