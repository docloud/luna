
Flask Principal
===============

*"I am that I am"*


Introduction
------------

Flask-Principal 提供一个极其松散的框架用于绑定两种类型的服务到 ``provider`` 上, 通常安置在一个Web应用的两个部分上:

    1. 验证 providers
    2. 用户信息 providers

举个例子, 一个验证 provider 可能是 oauth, 使用 Flask-OAuth 并且这个用户信息也许被存储在一个关系型数据库中. 这个框架的松藕合性是以信号作为接口来实现的.

The major components are the Identity, Needs, Permission, and the IdentityContext.

    1. The Identity represents the user, and is stored/loaded from various
       locations (eg session) for each request. The Identity is the user's
       avatar to the system. It contains the access rights that the user has.
    
    2. A Need is the smallest grain of access control, and represents a specific
       parameter for the situation. For example "has the admin role", "can edit
       blog posts".
    
       Needs are any tuple, or probably could be object you like, but a tuple
       fits perfectly. The predesigned Need types (for saving your typing) are
       either pairs of (method, value) where method is used to specify
       common things such as `"role"`, `"user"`, etc. And the value is the
       value. An example of such is `('role', 'admin')`. Which would be a
       Need for a admin role. Or Triples for use-cases such as "The permission
       to edit a particular instance of an object or row", which might be represented
       as the triple `('article', 'edit', 46)`, where 46 is the key/ID for that
       row/object.
       
       Essentially, how and what Needs are is very much down to the user, and is
       designed loosely so that any effect can be achieved by using custom
       instances as Needs.

       Whilst a Need is a permission to access a resource, an Identity should
       provide a set of Needs that it has access to.

    3. A Permission is a set of requirements, any of which should be
       present for access to a resource.
       
    4. An IdentityContext is the context of a certain identity against a certain
       Permission. It can be used as a context manager, or a decorator.


.. graphviz::


    digraph g {
        rankdir="LR" ;
        node [ colorscheme="pastel19" ];
        fixedsize = "true" ;
        i [label="Identity", shape="circle" style="filled" width="1.5", fillcolor="1"] ;
        p [label="Permission", shape="circle" style="filled" width="1.5" fillcolor="2"] ;
        n [label="<all> Needs|{<n1>RoleNeed|<n2>ActionNeed}", shape="Mrecord" style="filled" fillcolor="3"] ;
        c [label="IdentityContext", shape="box" style="filled,rounded" fillcolor="4"] ;
        p -> n:all ;
        c -> i ;
        c -> p ;
        i -> n:n1 ;
        i -> n:n2 ;

    }



Links
-----

* `documentation <http://packages.python.org/Flask-Principal/>`_
* `source <http://github.com/mattupstate/flask-principal>`_
* :doc:`changelog </changelog>`

Protecting access to resources
------------------------------

对于 Flask-Principal 的用户(不是认证的 providers), 访问控制很容易被同时定为一个 ``decorator`` 和一个 ``context manager`` . 正有一个带注释的简单快速入门示例::

    from flask import Flask, Response
    from flask.ext.principal import Principal, Permission, RoleNeed

    app = Flask(__name__)

    # load the extension
    principals = Principal(app)

    # Create a permission with a single Need, in this case a RoleNeed.
    admin_permission = Permission(RoleNeed('admin'))

    # protect a view with a principal for that need
    @app.route('/admin')
    @admin_permission.require()
    def do_admin_index():
        return Response('Only if you are an admin')

    # this time protect with a context manager
    @app.route('/articles')
    def do_articles():
        with admin_permission.require():
            return Response('Only if you are admin')

认证 providers
------------------------

认证 providers 应该使用 `identity-changed` 信号来指示这个请求已经被认证. 举个例子, 下面的代码是一个说明如何将 ``Flask-Principal`` 与一个常用的扩展 `Flask-Login <http://packages.python.org/Flask-Login/>`_ 相结合的模拟示例::


    from flask import Flask, current_app, request, session
    from flask.ext.login import LoginManager, login_user, logout_user, \
         login_required, current_user
    from flask.ext.wtf import Form, TextField, PasswordField, Required, Email
    from flask.ext.principal import Principal, Identity, AnonymousIdentity, \
         identity_changed

    app = Flask(__name__)

    Principal(app)

    login_manager = LoginManager(app)

    @login_manager.user_loader
    def load_user(userid):
        # Return an instance of the User model
        return datastore.find_user(id=userid)

    class LoginForm(Form):
        email = TextField()
        password = PasswordField()

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        # A hypothetical login form that uses Flask-WTF
        form = LoginForm()

        # Validate form input
        if form.validate_on_submit():
            # Retrieve the user from the hypothetical datastore
            user = datastore.find_user(email=form.email.data)
            
            # Compare passwords (use password hashing production)
            if form.password.data == user.password:
                # Keep the user info in the session using Flask-Login
                login_user(user)

                # Tell Flask-Principal the identity changed
                identity_changed.send(current_app._get_current_object(),
                                      identity=Identity(user.id))

                return redirect(request.args.get('next') or '/')
        
        return render_template('login.html', form=form)

    @app.route('/logout')
    @login_required
    def logout():
        # Remove the user information from the session
        logout_user()

        # Remove session keys set by Flask-Principal
        for key in ('identity.name', 'identity.auth_type'):
            session.pop(key, None)

        # Tell Flask-Principal the user is anonymous
        identity_changed.send(current_app._get_current_object(),
                              identity=AnonymousIdentity())

        return redirect(request.args.get('next') or '/')


用户信息 providers
--------------------------

用户信息 providers 应该连接到 `identity-loaded` 信号来添加一切附加信息到 Identity 实例、比如 roles. 下面是另一个使用 Flask-Login 的假设示例, 并且能和上一个例子相结合. 它表现了应该如何使用一个基于角色的权限表::

    from flask.ext.login import current_user
    from flask.ext.principal import identity_loaded, RoleNeed, UserNeed

    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        # Set the identity user object
        identity.user = current_user

        # Add the UserNeed to the identity
        if hasattr(current_user, 'id'):
            identity.provides.add(UserNeed(current_user.id))

        # Assuming the User model has a list of roles, update the 
        # identity with the roles that the user provides
        if hasattr(current_user, 'roles'):
            for role in current_user.roles:
                identity.provides.add(RoleNeed(role.name))


粗粒度的权限保护
----------------

现在让我们说, 举个例子, 你只想让博客帖子的作者编辑文章. 这个可以通过创建必需的 `Need` 和 
`Permission` 对象来实现, 并且添加更多逻辑到 `identity_loaded` 信号函数上, 举个例子::

    from collections import namedtuple
    from functools import partial

    from flask.ext.login import current_user
    from flask.ext.principal import identity_loaded, Permission, RoleNeed, \
         UserNeed

    BlogPostNeed = namedtuple('blog_post', ['method', 'value'])
    EditBlogPostNeed = partial(BlogPostNeed, 'edit')

    class EditBlogPostPermission(Permission):
        def __init__(self, post_id):
            need = EditBlogPostNeed(unicode(post_id))
            super(EditBlogPostPermission, self).__init__(need)

    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        # Set the identity user object
        identity.user = current_user

        # Add the UserNeed to the identity
        if hasattr(current_user, 'id'):
            identity.provides.add(UserNeed(current_user.id))

        # Assuming the User model has a list of roles, update the 
        # identity with the roles that the user provides
        if hasattr(current_user, 'roles'):
            for role in current_user.roles:
                identity.provides.add(RoleNeed(role.name))

        # Assuming the User model has a list of posts the user
        # has authored, add the needs to the identity
        if hasattr(current_user, 'posts'):
            for post in current_user.posts:
                identity.provides.add(EditBlogPostNeed(unicode(post.id)))

下一步是保护这个 endpoint 允许某个用户编辑一篇文章. 这是通过使用资源ID即时创建权限(Permission)对象来进行的 , 在这个博客文章例子中::

    @app.route('/posts/<post_id>', methods=['PUT', 'PATCH'])
    def edit_post(post_id):
        permission = EditBlogPostPermission(post_id)

        if permission.can():
            # Save the edits ...
            return render_template('edit_post.html')

        abort(403)  # HTTP Forbidden


API
===



Starting the extension
----------------------

.. autoclass:: flask_principal.Principal
    :members:


Main Types
----------

.. autoclass:: flask_principal.Permission
    :members:

.. autoclass:: flask_principal.Identity
    :members:

.. autoclass:: flask_principal.AnonymousIdentity
    :members:

.. autoclass:: flask_principal.IdentityContext
    :members:



Predefined Need Types
---------------------

.. autoclass:: flask_principal.Need

.. autoclass:: flask_principal.RoleNeed

.. autoclass:: flask_principal.UserNeed

.. autoclass:: flask_principal.ItemNeed


Signals
----------------

.. data:: identity_changed

   Signal sent when the identity for a request has been changed.

.. data:: identity_loaded

   Signal sent when the identity has been initialised for a request.

.. _Flask documentation on signals: http://flask.pocoo.org/docs/signals/


Changelog
=========
.. toctree::
   :maxdepth: 2

   changelog


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

