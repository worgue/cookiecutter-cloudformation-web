# cookiecutter cloudformation template for webapp

※とりあえずの、テストアップです。

クラウドフォーメーションのテンプレートは、十分な機能を持ったものがAmazonのサンプルとして手に入りますが、規模が大きすぎると構成要素の把握が困難です。
このプロジェクトは、webサイトのデプロイに特化し、最小限のクラウドフォーメーションのテンプレートを出力する、cookiecutterのテンプレートです。
出来るだけ、クラウドフォーメーションの側での変数設定を省き、自分が必要とするAWS構成要素をymlとして確認できることを目的としています。

## cookiecutterのパラメタ一覧
app_service
```````````

ec2かfargate、どちらのテンプレートを出力するか選べます


app_subnets
```````````

appがPUBLICもしくはPRIVATEどちらのサブネットにデプロイされるか選べます。


use_efs
```````

efs用のセキュリティグループとボリュームを作成します。

use_rds
```````

rds用のセキュリティグループを作成します。rds自体は作成しません。

use_cache
`````````

cache用のセキュリティグループを作成します。cache自体は作成しません。


use_certificate
```````````````

ロードバランサー作成時に証明書を作成します。route53で管理されたドメインにデプロイする必要があります。

use_iprestriction
`````````````````

アプリケーションの任意のパスに、特定のIP制限をかける場合に利用します。



## Usage
### get cloudformation templates
```
$ cookiecutter ...
```

### create AWS Resources


#### AWS management console


