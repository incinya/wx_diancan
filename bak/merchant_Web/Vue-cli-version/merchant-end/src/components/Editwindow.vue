<style>
	h2 {
		font-size: 25px;
	}
	p {
		font-size: 15px;
		margin: 5px;
	}
	#photo {
		margin-top: 20px;
		width: 180px;
		height: 180px;
		background-color: gray;
		margin-left: auto;
		margin-right: auto;
	}
</style>


<template>

	<div>
		<Row span="24">
		<Col span="8">
			<div id="photo">
				<img :src="srcimage" style="height:100%;width:100%;">
			</div>
			<br/><br/>
			<Upload action="/api/upload_image" style="float:right; margin-right:24px;" :on-success="handleSuccess" name="image" ref="upload" :before-upload="reset">
				<Tooltip content="图片名称不能包含中文字符" placement="left">
				<Button type="ghost" icon="ios-cloud-upload-outline">上传图片</Button>
				</Tooltip>
			</Upload>

		</Col>
		<Col span="16">
			
			<p style="float: left">菜品名称</p>
			<br></br>
			<Tooltip content="菜品名称不能包含中文字符" placement="right-start">
			<Input placeholder="请输入菜名..." :autofocus="true" @on-change="DeliverData" v-model="srcdishname"></Input>
			</Tooltip>
			<p>菜品描述</p>
			<Tooltip content="菜品描述不能包含中文字符" placement="right-start">
			<Input placeholder="请输入描述..." :autofocus="true" @on-change="DeliverData" v-model="srcdescription" type="textarea" :rows="5" ></Input>
			</Tooltip>
			<p>定价</p>
			<Tooltip content="请输入数字" placement="right-start">
			<Input placeholder="请输入..." :autofocus="true" @on-change="DeliverData" v-model="srcdishprice"></Input>
			</Tooltip>
		</Col>
		</Row>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				upload_finished:false,
			}
		},
		props: ['srcdishname', 'srcdescription', 'srcdishprice', 'srcimage'],
		methods: {
			DeliverData() {
				let data = {
					EditedName: this.srcdishname,
					EditedDescription: this.srcdescription,
					EditedPrice: this.srcdishprice,
					EditedImage: this.srcimage
				};
				this.$emit('UpdateDish', data);
			},
			handleSuccess(res, file) {
				console.log(res);
				console.log(file);
				this.srcimage = 'http://' + res.url;
				this.upload_finished = true;
				this.DeliverData();
				console.log(this.srcimage);
			},
			reset() {
				this.$refs.upload.clearFiles();
			}
		}
	}
</script>