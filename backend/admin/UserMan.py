from . import admin_bp
from flask import render_template, g, session, request, redirect, url_for
from backend.models import User, workrel
from backend import db

# 解决操作员bug
@admin_bp.route("/manage")
def manage():
    # 获得参数发送过来的总监
    manId = request.args.get("manId")
    # 获得参数发送过来的经理
    lowId = request.args.get("lowId")
    # 获得参数传送过来的员工
    workerId = request.args.get("workerId")
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
    workerList = []
    if manId or lowId or workerId:
        midMans = User.query.filter_by(level=32).all()
        if manId:
            lowMans = getUpMen(manId)
            for lowman in lowMans:
                workerList.extend(getUpMen(lowman.account))
                for workersl in workerList:
                    lineWorkers.extend(getUpMen(workersl.account))
                    # lineWorkers =
        if lowId:
            # midMans = User.query.filter_by(level=32).all()
            lowMans = User.query.filter_by(account=lowId).all()

            workerList = getUpMen(lowId)
            for workersl in workerList:
                lineWorkers.extend(getUpMen(workersl.account))
        if workerId:
            workerList = User.query.filter_by(account=workerId).all()
            print(workerList[0].maccount)
            lowMans = User.query.filter_by(id=workerList[0].maccount).all()
            lineWorkers = getUpMen(workerId)
        else:
            pass
    else:
        # 获得所有用户
        users = User.query.all()
        midMans = User.query.filter_by(level=32).all()
        # 获得第一个总监的经理
        if midMans:
            lowMans = getUpMen(midMans[0].account)
        if workerList:
            workerList = getUpMen(lowMans[0].account)
        if lineWorkers:
            lineWorkers = getUpMen(workerList[0].account)
        # print(workers)
        if not users is None:
            # 获得所有员工
            numSum = len(users)
            for user in users:
                if user.level == 64:
                    continue
                else:
                    if user.maccount is None:
                        disconttrolNum += 1
                        disconttrol.append(user)
                    # elif user.level == 32:
                    #     midMans.append(user)
                    # elif user.level == 16:
                    #     lowMans.append(user)
                    # elif user.level == 8:
                    #     workerList.append(user)
                    # elif user.level == 4:
                    #     lineWorkers.append(user)
                    else:
                        pass

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
        # 为用户添加上属
        man = User.query.filter_by(account=account).first()
        man.maccount = manAccount
        db.session.add(man)
        # 为管理添加下属
        rel = workrel()
        rel.create(workerId=account, manageId=manAccount)
        db.session.add(rel)
        db.session.commit()
        return redirect(url_for("admin.manage"))

    else:
        if account:
            user = User.query.filter_by(account=account).first()
            if user.level > 2:
                manlevel = user.level << 1
            else:
                manlevel = 4
            # print(manlevel, user.level)
            mans = User.query.filter_by(level=manlevel).all()
            return render_template("admin/editMan.html", user=user, mans=mans)
        else:
            return render_template("admin/index.html")


# 根据管理员账号获得管理人员
def getUpMen(mAcoount):
    lowManList = []
    lowMans = []
    users = User.query.filter_by(account=mAcoount).first()
    lowMan = users.manId.all()
    if lowMan:
        lowMans = [man.workerId for man in lowMan]
    # print(lowMans)
    lowManList = User.query.filter(User.account.in_(lowMans)).all()
    return lowManList
