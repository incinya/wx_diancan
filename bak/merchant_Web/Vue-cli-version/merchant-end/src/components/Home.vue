<style scoped>
    .layout-con{
        height: 100%;
        width: 100%;
    }
    .menu-item span{
        display: inline-block;
        overflow: hidden;
        width: 69px;
        text-overflow: ellipsis;
        white-space: nowrap;
        vertical-align: bottom;
        transition: width .2s ease .2s;
    }
    .menu-item i{
        transform: translateX(0px);
        transition: font-size .2s ease, transform .2s ease;
        vertical-align: middle;
        font-size: 16px;
    }
    .collapsed-menu span{
        width: 0px;
        transition: width .2s ease;
    }
    .collapsed-menu i{
        transform: translateX(5px);
        transition: font-size .2s ease .2s, transform .2s ease .2s;
        vertical-align: middle;
        font-size: 22px;
    }
    #logo {
    overflow: hidden;
}
</style>
<template>
    <div class="layout">
        <Layout :style="{minHeight: '100vh'}">
            <Sider>
                <div id="logo" style="width: auto; height: 64px;">
                    <img src="../assets/MerchantLogo3.png" alt="logo" style="height:100%;width:100%;">
                </div>
                <Menu active-name="1-1" theme="dark" width="auto" :open-names="['1']">
                    <Submenu name="1">
                        <template slot="title">
                            <Icon type="ios-analytics"></Icon>
                                导航栏
                        </template>
                    <MenuGroup title="餐厅管理">
                        <router-link to="/home/restaurantinfo">
                            <MenuItem name="1-1">餐厅信息</MenuItem>
                        </router-link>
                        <router-link to="/home/menu">
                            <MenuItem name="1-2">菜单管理</MenuItem>
                        </router-link>
                        <router-link to="/home/order">
                            <MenuItem name="1-3">订单管理</MenuItem>
                        </router-link>
                    </MenuGroup>
                    <MenuGroup title="个人中心">
                        <router-link to="/home/generate_qrcode">
                        <MenuItem name="2-1">定制餐桌二维码</MenuItem>
                        </router-link>
                        <MenuItem name="2-2">设置</MenuItem>
                    </MenuGroup>
                     </Submenu>
                </Menu>
            </Sider>
            <Layout>
                    <Menu mode="horizontal" :theme="theme1" style="height:65px;">
                        <MenuItem name="1" style="float:right;">
                            <Avatar src="https://ss0.baidu.com/6ONWsjip0QIZ8tyhnq/it/u=123308412,2828093194&fm=58"/>
                        </MenuItem>
                        <MenuItem name="2" style="float:right">
                            <Badge dot>
                                <Icon type="gear-b" size="26"></Icon>
                            </Badge>
                        </MenuItem>
                        <MenuItem name="2" style="float:right">
                            <Badge count="3">
                                <Icon type="email" size="26"></Icon>
                            </Badge>
                        </MenuItem>
                    </Menu>
                <router-view></router-view>
            </Layout>
        </Layout>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                theme1:'light'
            }
        }
    }
</script>
