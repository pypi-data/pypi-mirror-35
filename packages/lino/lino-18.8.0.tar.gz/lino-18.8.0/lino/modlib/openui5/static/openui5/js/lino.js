/*
*
*  This is for global shortcuts and javascript: hrefs for actions and routing
*  Currently is static, but might change to a template in needed.
*  Included in main.html
*
*/

Lino = {
    window_action: function(){
        sap.ui.getCore().byId("__component0---MAIN_VIEW").getController().routeToAction(...arguments);
    },

    /**
     * Generalised ajax caller for simple actions.
     * @param actor_id
     * @param action_name
     * @param rp
     * @param is_on_main_actor
     * @param pk
     * @param params
     */
    simple_action: function (actor_id, action_name, rp, is_on_main_actor, pk, params) {
        console.log(arguments);
    },

    /**
     * Generalised ajax caller for param action, which need to open a dialog for action parameters.
     * The name of the view should be generated from actor_id and action_name.
     * @param actor_id
     * @param action_name
     * @param rp
     * @param params
     */
    param_action: function (actor_id, action_name, rp, params) {
        console.log(arguments);
    },
    /**
     * Connect as an other user.
     * @param id
     * @param name
     */
    set_subst_user: function (id, name) {
        sap.ui.getCore().byId("__component0---MAIN_VIEW").getController().set_subst_user(id);
        Lino.current_window.main_item.set_base_param("{{constants.URL_PARAM_SUBST_USER}}", id);
    }


};