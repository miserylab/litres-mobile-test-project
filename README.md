# Test automation project for [Litres](https://www.litres.ru/o-kompanii/) mobile app

![Litres logo](https://user-images.githubusercontent.com/95403808/201316165-1731965e-bf09-4dae-82d7-1789b6e8eef6.png)

> LitRes is an international company that produces and distributes e-books and digital audiobooks.

# <a name="TableOfContents">Table of contents</a>
+ [Description](#Description)
+ [Tools and technologies](#Technology)
+ [How to run](#Jenkins)
    + [Gradle command](#GradleCommand)
    + [Property files](#PropertyFiles)
      + [Default property files](#PropertyFilesDefaults)
    + [Run in Jenkins](#RunInJenkins)
+ [Telegram Notifications](#TelegramNotifications)
+ [Test results report in Allure Report](#AllureReport)
+ [Allure TestOps integration](#AllureTestOps)
    + [Project in Allure TestOps](#AllureTestOpsProject)
    + [Start a run of custom set of tests](#AllureTestOpsStartTests)
    + [Dashboards](#Dashboards)
    + [Defects](#Defects)
+ [GitHub webhooks](#GithubWebhooks)
+ [Jira integration](#Jira)
+ [Video of running tests](#Video)


# <a name="Description">Description</a>
The test project consists of mobile(android) tests.

# <a name="Technology">Tools and a technologies</a>
<p  align="center">
  <img src="resources/images/logo/python.svg" width="5%" alt="Python"/>
  <img src="resources/images/logo/selene.png" width="5%" alt="Selene"/>
  <img src="resources/images/logo/pytest.png" width="5%" alt="Pytest"/>
  <img src="resources/images/logo/pycharm.png" width="5%" alt="PyCharm"/>
  <img src="resources/images/logo/appium.svg" width="5%" alt="Appium"/>
  <img src="resources/images/logo/jenkins.png" width="5%" alt="Jenkins"/>
  <img src="resources/images/logo/selenoid.png" width="5%" alt="Selenoid"/>
  <img src="resources/images/logo/Allure.svg" width="5%"  alt="Allure"/>
  <img src="resources/images/logo/Allure_TO.svg" width="5%" alt="Allure TestOps"/>
  <img src="resources/images/logo/browserstack.svg" width="5%" alt="Browserstack"/>
  <img src="resources/images/logo/telegram.svg"width="5%" alt="Telegram"/>
</p>

The autotests in this project are written in `Python` using `Selene` framework.\
`Jenkins` - CI/CD for running tests remotely.\
`Browserstack` - to run mobile tests.\
`Android Studio tools`, `Appium` - to tun mobile tests locally in a mobile device emulator.\
`Allure Report` - for test results visualisation.\
`Telegram Bot` - for test results notifications.\
`Allure TestOps` - as Test Management System.

[Back to the table of contents ⬆](#TableOfContents)

# <a name="HowToRun">How to run</a>

To run locally with config.personal.env (create it first) the following command is used:
```bash
env -S 'context=emulation' pytest tests/android/test_login.py --alluredir reports/
```
To run in Browserstack and in Jenkins with config.browserstack.env the following command is used:
```bash
env -S 'context=browserstack' pytest tests/android/test_login.py --alluredir reports/
```

[Back to the table of contents ⬆](#TableOfContents)

## <a name="ConfigFiles">Config files</a>
Possible properties in a config file:
```properties
platformName=
platformVersion=
deviceName=
app=
remote_url=
user_name=
access_key=
projectName=
buildName=
sessionName=
appWaitActivity=
systemPort=
```

[Back to the table of contents ⬆](#TableOfContents)

### <a name="CongigFileExample">Config file examples</a>


* <details>
    <summary><h4>config.browserstack.env.example</h4></summary>

    ```congig
        platformName='android'
        platformVersion='11.0'
        deviceName='Google Pixel 4'
        app='app'
        remote_url='http://hub.browserstack.com/wd/hub'
        user_name='xxxa_QrzYPv'
        access_key='xxxxuBSKtK1F'
        projectName='First Python project'
        buildName='browserstack-build-1'
        sessionName='BStack first_test'

    ```
  
  </details>
* <details>
    <summary><h4>config.emulation.env.examples</h4></summary>

    ```properties
        app='./xxxx_3.66.0(0)-gp.apk'
        appWaitActivity='*.xxxxx.*'
        systemPort=8082
        autoGrantPermissions=false
    ```

  </details>



[Back to the table of contents ⬆](#TableOfContents)

## <a name="RunInJenkins">Run in [Jenkins](https://jenkins.autotests.cloud/job/C12-vyach_son-bookmate_test/)</a>
Main page of the build:
<p  align="center">
<img src="images/screens/JenkinsBuildMainPage.png" alt="JenkinsBuildMainPage" width="950">
</p>

A parametrized Jenkins job can be launched with needed ***tag*** and ***runIn***:
<p  align="center">
<img src="images/screens/JenkinsBuildParameters.gif" alt="JenkinsBuildParameters" width="950">
</p>

`project-{runIn}.properties` config files are created in the build workspace on start build.

Sensitive information(login names and passwords) is stored in an encrypted form in Jenkins credential storage.\
And relatively safe transferred to the build by gradle arguments(see [Gradle command](#GradleCommand) section, 'Additional parameters') and it's values masked in the logs.

After the build is done the test results are available in:
>- <code><strong>*Allure Report*</strong></code>
>- <code><strong>*Allure TestOps*</strong></code> - results are uploaded there and the automated test-cases can be automatically updated accordingly to the recent changes in the code.

<p  align="center">
<img src="images/screens/JenkinsFinishedBuild.png" alt="JenkinsFinishedBuild" width="950">
</p>

[Back to the table of contents ⬆](#TableOfContents)


# <a name="TelegramNotifications">Telegram Notifications</a>
Telegram bot sends a brief report to a specified telegram chat by results of each build.
<p  align="center">
<img src="images/screens/TelegramNotification.png" alt="TelegramNotification" width="550">
</p>

[Back to the table of contents ⬆](#TableOfContents)

# <a name="AllureReport">Test results report in [Allure Report](https://jenkins.autotests.cloud/job/C12-vyach_son-bookmate_test/47/allure/)</a>

## Main page
Main page of Allure report contains the following blocks:

>- <code><strong>*ALLURE REPORT*</strong></code> - displays date and time of the test, overall number of launched tests, а также диаграмму с указанием процента и количества успешных, упавших и сломавшихся в процессе выполнения тестов
>- <code><strong>*TREND*</strong></code> - displays trend of running tests for all runs
>- <code><strong>*SUITES*</strong></code> - displays distribution of tests by suites
>- <code><strong>*CATEGORIES*</strong></code> - displays distribution of unsuccessful tests by defect types
<p align="center">
  <img src="images/screens//AllureReportMain.png" alt="AllureReportMain" width="950">
</p>

## List of tests with steps and test artefacts
On the page the list of the tests grouped by suites with status shown for each test.\
Full info about each test can be shown: tags, severity, duration, detailed steps.

<p align="center">
  <img src="images/screens/AllureReportSuites.png" alt="AllureReportSuites" width="1150">
</p>

Also additional test artifacts are available:
>- Screenshot
>- Page Source
>- Video
>- Browserstack full info link

<p align="left">
  <img src="images/screens/AllureReportSuites2.png" alt="AllureReportSuites2" width="950">
</p>

[Back to the table of contents ⬆](#TableOfContents)

# <a name="AllureTestOps">[Allure TestOps](https://allure.autotests.cloud/project/1466/test-cases?treeId=2804) integration</a>
> The link can be accessed only by authorized users.

## <a name="AllureTestOpsProject">Project in Allure TestOps</a>
Test-cases in the project are imported and constantly updated from the code,
so there is no need in complex process of synchronization manual test-cases and autotests.\
It is enough to create and update an autotest in the code and the test-case in TMS always will be in actual state.\
Manual test-cases also can be added in TMS in case of need(via web interface or via code).
<p align="center">
  <img src="images/screens/AllureTestOpsTests.gif" alt="AllureTestOpsTests" width="1050">
</p>

```mermaid
stateDiagram-v2
state "Test created/updated in the code" as A
state "Build in Jenkins is triggered on push or started manually" as B
state "Jenkins build is done" as C
state "Allure TestOps launch related to the build marked as closed" as D
state "All executed test-cases are automatically created/updated according to the code" as E
[*] --> A
A --> B
B --> C
C --> D
D --> E
E --> A
```

## <a name="AllureTestOpsStartTests">Ability to start a run of custom set of tests from Allure TestOps</a>
Any person not related to autotest creation can select a set of tests, environment parameter(RunIn) and start a run.\
Allure TestOps run will be created, Jenkins job triggered with correct parameters. And results of the job will be seamlessly integrated into Allure TestOps.
<p align="center">
  <img src="images/screens/AllureTestOpsSelectionOfTests.gif" alt="AllureTestOpsSelectionOfTests" width="1050">
</p>

As soon as the Jenkins job is done, corresponding tests get their statuses. A tester can finish manual tests(if any) and click "Close launch".

<p align="center">
  <img src="images/screens/AllureTestOpsFinishedRunClickStop.png" alt="AllureTestOpsFinishedRunClickStop" width="1250">
</p>

> After that all these test-cases(names, steps, tags etc.) will be updated according to the recent code changes.

[Back to the table of contents ⬆](#TableOfContents)

## <a name="Dashboards">Dashboards</a>
Automation trends charts, distribution tests by some different parameters etc.:
<p align="center">
  <img src="images/screens/AllureTestOpsDashboardsOverview.png" alt="AllureTestOpsDashboardsOverview" width="1050">
</p>

<p align="center">
  <img src="images/screens/AllureTestOpsDashboardsAutomation.png" alt="AllureTestOpsDashboardsAutomation" width="1050">
</p>

<p align="center">
  <img src="images/screens/AllureTestOpsDashboardsMembers.png" alt="AllureTestOpsDashboardsMembers" width="1050">
</p>

<p align="center">
  <img src="images/screens/AllureTestOpsDashboardsAdditional.png" alt="AllureTestOpsDashboardsAdditional" width="1050">
</p>

[Back to the table of contents ⬆](#TableOfContents)

## <a name="Defects">Defects</a>
Knows defects are automatically recognized by defined patterns for test fails in further launches.
<p align="center">
  <img src="images/screens/AllureTestOpsDefects.png" alt="AllureTestOpsDefects" width="1050">
</p>

[Back to the table of contents ⬆](#TableOfContents)


# <a name="JiraIntegration">Jira integration</a>
<p align="center">
![image](https://user-images.githubusercontent.com/95403808/201317409-8c298de1-415b-4cf3-a8ce-cd2b27f252bd.png)  
</p>

[Back to the table of contents ⬆](#TableOfContents)


# <a name="Video">Video of running tests</a>

https://user-images.githubusercontent.com/95403808/201222870-cecfa7fa-3c09-4526-9298-4850feb7d600.mp4



[Back to the table of contents ⬆](#TableOfContents)



