//index.js
//获取应用实例
const app = getApp()

Page({
  data: {
    tabIndex: 0,
    // 统计商品数量和价格
    orderCount: {
      num: 0,
      money: 0
    },
    bottomFlag: false,
    // 提交的订单
    orders: true,
    menus: [{
      id: 1,
      menu: '所有菜品'
    }, 
    // {
      // id: 2,
      // menu: '折扣'
    // },
     {
      id: 3,
      menu: '特色小龙虾'
    }, {
      id: 4,
      menu: '精品家常菜'
    }, {
      id: 5,
      menu: '干锅系列'
    }, {
      id: 6,
      menu: '炒饭系列'
    }, ],
    // 商品列表

  },


  // 下拉刷新
  onPullDownRefresh: function() {
    setTimeout(() => {
      wx.showToast({
        title: '成功加载数据',
        icon: 'success',
        duration: 500
      });
      wx.stopPullDownRefresh()
    }, 500);
  },



  tabMenu: function(event) {
    var that = this
    let index = event.target.dataset.index;
    let aa = this.data.tmp
    let bb = []
    for (var inde in aa) {

      if (event.target.dataset.id == aa[inde].menuId) {

        bb.push(aa[inde])
      }
      if (event.target.dataset.id == aa[inde].bargin) {
        bb.push(aa[inde])
      }
      if (event.target.dataset.id == '所有菜品') {
        bb.push(aa[inde])
      }
    }
    
    that.setData({
      tabIndex: index,
      items: bb,
    });
  },


  // 点击去购物车结账
  card: function() {
    let that = this;
    // 判断是否有选中商品
    if (that.data.orderCount.num !== 0) {
      // 跳转到购物车订单也
      wx.redirectTo({
        url: '../order/order'
      });
    } else {
      wx.showToast({
        title: '您未选中任何商品',
        icon: 'none',
        duration: 2000
      })
    }
  },
  addOrder: function(event) {
    let that = this;
    let id = event.target.dataset.id;
    let index = event.target.dataset.index;
    let param = this.data.items[index];
    let subOrders = []; // 购物单列表存储数据
    param.active ? param.active = false : param.active = true;
    // 改变添加按钮的状态
    this.data.items.splice(index, 1, param);
    that.setData({
      items: this.data.items
    });
    // 将已经确定的菜单添加到购物单列表

    // console.log(this.data.items)
    

    this.data.items.forEach(item => {
      if (item.active) {
        subOrders.push(item);
      }
    });

    // 判断底部提交菜单显示隐藏
    if (subOrders.length == 0) {
      that.setData({
        bottomFlag: false
      });
    } else {
      that.setData({
        bottomFlag: true
      });
    }
    let money = 0;
    let num = subOrders.length;
    subOrders.forEach(item => {
      money += item.price; // 总价格求和
    });
    let orderCount = {
      num,
      money
    }
    // 设置显示对应的总数和全部价钱
    this.setData({
      orderCount
    });
    // 将选中的商品存储在本地
    wx.setStorage({
      key: "orders",
      data: subOrders
    });
  },
  onLoad: function() {
    
    var that = this
    remote: wx.request({
      // url: 'http://192.168.0.112:8000/index/main/',
      url: 'http://176.209.103.15:8000/index/main/',
      
      success(res) {
        
        that.setData({
          items: res.data.items,
          tmp : res.data.items
        })
      }
    })
  }
})