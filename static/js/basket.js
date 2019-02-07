let config = {
    selectors: {
        add: '.basket-item-add',
        remove: '.basket-item-remove',
        delete: '.basket-item-delete',
        quantity: '.basket-item-quantity',
    },
    urls: {
        add: '/basket/add/',
        remove: '/basket/remove/',
        delete: '/basket/delete/',
    }
};

$(document).ready(function () {

    $(config.selectors.add).on('click', function () {
        let item_id = $(this).data('id');
        let parent_item = $(this).parents()[0];
        let counter = $(parent_item).find(config.selectors.quantity);

        let item_url = config.urls.add + item_id + '/';

        $.ajax({
            url: item_url,

            success: function (data) {
                counter.text(data.quantity)
            }
        });
    });
    $(config.selectors.remove).on('click', function () {
        let item_id = $(this).data('id');
        let parent_item = $(this).parents()[0];
        let counter = $(parent_item).find(config.selectors.quantity);
        let item_url = config.urls.remove + item_id + '/';

        $.ajax({
            url: item_url,

            success: function (data) {
                if (data.quantity > 0) {
                    counter.text(data.quantity)
                } else {
                    $(parent_item).hide()
                }
            }
        });
    });
    $(config.selectors.delete).on('click', function () {
        let item_id = $(this).data('id');
        let parent_item = $(this).parents()[0];

        let item_url = config.urls.delete + item_id + '/';

        $.ajax({
            url: item_url,

            success: function () {
                $(parent_item).hide()
            }
        });
    })
});