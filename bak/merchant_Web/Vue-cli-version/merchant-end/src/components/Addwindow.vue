<style>

</style>
<template>
	<div>
		<Row span="24">
		<Col span="8">
			<div id="photo" v-if="upload_finished==true">
				<img :src="this.image_url" style="height:100%;width:100%;">
			</div>
			<br/><br/>
			<Upload action="/api/upload_image" style="float:right; margin-right:24px;" :on-success="handleSuccess" name="image" ref="upload">
				<Tooltip content="图片名称不能包含中文字符" placement="left">
				<Button type="ghost" icon="ios-cloud-upload-outline">上传图片</Button>
				</Tooltip>
			</Upload>
		</Col>
		<Col span="16">
			<div>
				<p style="float: left">菜品名称</p>
				<br></br>
				<Tooltip content="菜品名称不能包含中文字符" placement="right-start">
				<Input placeholder="请输入菜名..." :autofocus="true" @on-change="DeliverData" v-model="srcdishname"></Input>
				</Tooltip>
			</div>
			<p style="float: left">菜品描述</p>
			<br></br>
			<Tooltip content="菜品描述不能包含中文字符" placement="right-start">
			<Input placeholder="请输入菜品描述..." :autofocus="true" @on-change="DeliverData" v-model="srcdescription" type="textarea" :rows="5" ></Input>
			</Tooltip>
			<p>定价</p>
			<Tooltip content="请输入数字" placement="right-start">
			<Input placeholder="请输入菜品定价..." :autofocus="true" @on-change="DeliverData" v-model="srcdishprice"></Input>
			</Tooltip>
		</Col>

		</Row>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				image_url:'',
				upload_finished:false,
				srcdishname:'',
				srcdescription:'',
				srcdishprice:''
			}
		},
		methods: {
			DeliverData() {
				let data = {
					EditedName: this.srcdishname,
					EditedDescription: this.srcdescription,
					EditedPrice: this.srcdishprice,
					EditedImage: this.image_url
				};
				this.$emit('AddNewDish', data);
			},
			handleSuccess (res, file) {
				console.log(res);
				console.log(file);
				this.image_url = 'http://' + res.url;
				this.upload_finished = true;
				this.DeliverData();
				this.$refs.upload.clearFiles();
			},
			reset() {
				this.upload_finished=false;
				this.$refs.upload.clearFiles();
				this.image_url='';
				this.srcdishprice='';
				this.srcdescription='';
				this.srcdishname='';
			}
		}
	}
</script>