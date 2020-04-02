from . import admin_bp
from flask import render_template, g, session, request, redirect, url_for
from backend.models import User, workrel
from backend import db

# 解决操作员bug
@admin_bp.route("/manage")
def manage():
    numSum = 0
    customerSum = 0
    workersSum = 0
    midMansSum = 0
    lowMansSum = 0
    lineWorkersSum = 0
    workers = []
    midMans = []
    lowMans = []
    lineWorkers = []
    disconttrolNum = 0
    disconttrol = []
    # 获得所有用户
    users = User.query.all()
    midManers = User.query.filter_by(level=32).all()
    # print(midManer.manId.all())
    # 判断是否存在总监
    if midManers:
        # 获得第一个总监
        midManer = midManers[0]
        # 获得第一个总监管理的所有经理
        lowMans = midManer.manId.all()
        # 如果有经理的话
        if len(lowMans) != 0:
            # 获得经理人数
            lowMansSum = len(lowMans)
            # 获得经理的account
            lowManList = [lowman.workerId for lowman in lowMans]
            # print(lowManList)
            # 获得经理的对象
            lowMans = User.query.filter(User.account.in_(lowManList)).all()
            # 操作员列表
            workerList = []
            if lowMans:
                for lowMan in lowMans:
                    for worker in lowMan.manId.all():
                        workerList.append(worker.workerId)
                        workersSum += 1
            print(workerList)
    if not users is None:
        # 获得所有员工
        numSum = len(users)
        for user in users:
            if user.level == 32:
                midMansSum += 1
                midMans.append(user)
            elif len(user.manId.all()) == 0:
                print("s")
                disconttrolNum += 1
                disconttrol.append(user)

    return render_template(
        "admin/manUser.html",
        numSum=numSum,
        customerSum=customerSum,
        workersSum=workersSum,
        midMansSum=midMansSum,
        lowMansSum=lowMansSum,
        lineWorkersSum=lineWorkersSum,
        workers=workerList,
        midMans=midMans,
        lowMans=lowMans,
        lineWorkers=lineWorkers,
        disconttrolNum=disconttrolNum,
        disconttrol=disconttrol,
    )


@admin_bp.route("/manage/edit/<account>", methods=["GET", "POST"])
def manageEdit(account):
    if request.method == "POST":
        # print(request.form)
        account = request.form["account"]
        # password = request.form['']
        manAccount = request.form["manage"]
        man = User.query.filter_by(account=manAccount).first()
        rel = workrel()
        rel.create(workerId=account, manageId=man.id)
        db.session.add(rel)
        db.session.commit()
        return redirect(url_for("admin.manage"))

    else:
        if account:
            user = User.query.filter_by(account=account).first()
            manlevel = user.level << 1
            # print(manlevel, user.level)
            mans = User.query.filter_by(level=manlevel).all()
            return render_template("admin/editMan.html", user=user, mans=mans)
        else:
            return render_template("admin/index.html")
