'''
# AWS Backup Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

AWS Backup is a fully managed backup service that makes it easy to centralize and automate the
backup of data across AWS services in the cloud and on premises. Using AWS Backup, you can
configure backup policies and monitor backup activity for your AWS resources in one place.

## Backup plan and selection

In AWS Backup, a *backup plan* is a policy expression that defines when and how you want to back up
your AWS resources, such as Amazon DynamoDB tables or Amazon Elastic File System (Amazon EFS) file
systems. You can assign resources to backup plans, and AWS Backup automatically backs up and retains
backups for those resources according to the backup plan. You can create multiple backup plans if you
have workloads with different backup requirements.

This module provides ready-made backup plans (similar to the console experience):

```python
# Daily, weekly and monthly with 5 year retention
plan = backup.BackupPlan.daily_weekly_monthly5_year_retention(self, "Plan")
```

Assigning resources to a plan can be done with `addSelection()`:

```python
# plan: backup.BackupPlan

my_table = dynamodb.Table.from_table_name(self, "Table", "myTableName")
my_cool_construct = Construct(self, "MyCoolConstruct")

plan.add_selection("Selection",
    resources=[
        backup.BackupResource.from_dynamo_db_table(my_table),  # A DynamoDB table
        backup.BackupResource.from_tag("stage", "prod"),  # All resources that are tagged stage=prod in the region/account
        backup.BackupResource.from_construct(my_cool_construct)
    ]
)
```

If not specified, a new IAM role with a managed policy for backup will be
created for the selection. The `BackupSelection` implements `IGrantable`.

To add rules to a plan, use `addRule()`:

```python
# plan: backup.BackupPlan

plan.add_rule(backup.BackupPlanRule(
    completion_window=Duration.hours(2),
    start_window=Duration.hours(1),
    schedule_expression=events.Schedule.cron( # Only cron expressions are supported
        day="15",
        hour="3",
        minute="30"),
    move_to_cold_storage_after=Duration.days(30)
))
```

Continuous backup and point-in-time restores (PITR) can be configured.
Property `deleteAfter` defines the retention period for the backup. It is mandatory if PITR is enabled.
If no value is specified, the retention period is set to 35 days which is the maximum retention period supported by PITR.
Property `moveToColdStorageAfter` must not be specified because PITR does not support this option.
This example defines an AWS Backup rule with PITR and a retention period set to 14 days:

```python
# plan: backup.BackupPlan

plan.add_rule(backup.BackupPlanRule(
    enable_continuous_backup=True,
    delete_after=Duration.days(14)
))
```

Ready-made rules are also available:

```python
# plan: backup.BackupPlan

plan.add_rule(backup.BackupPlanRule.daily())
plan.add_rule(backup.BackupPlanRule.weekly())
```

By default a new [vault](#Backup-vault) is created when creating a plan.
It is also possible to specify a vault either at the plan level or at the
rule level.

```python
my_vault = backup.BackupVault.from_backup_vault_name(self, "Vault1", "myVault")
other_vault = backup.BackupVault.from_backup_vault_name(self, "Vault2", "otherVault")

plan = backup.BackupPlan.daily35_day_retention(self, "Plan", my_vault) # Use `myVault` for all plan rules
plan.add_rule(backup.BackupPlanRule.monthly1_year(other_vault))
```

You can [backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/windows-backups.html)
VSS-enabled Windows applications running on Amazon EC2 instances by setting the `windowsVss`
parameter to `true`. If the application has VSS writer registered with Windows VSS,
then AWS Backup creates a snapshot that will be consistent for that application.

```python
plan = backup.BackupPlan(self, "Plan",
    windows_vss=True
)
```

## Backup vault

In AWS Backup, a *backup vault* is a container that you organize your backups in. You can use backup
vaults to set the AWS Key Management Service (AWS KMS) encryption key that is used to encrypt backups
in the backup vault and to control access to the backups in the backup vault. If you require different
encryption keys or access policies for different groups of backups, you can optionally create multiple
backup vaults.

```python
my_key = kms.Key.from_key_arn(self, "MyKey", "aaa")
my_topic = sns.Topic.from_topic_arn(self, "MyTopic", "bbb")

vault = backup.BackupVault(self, "Vault",
    encryption_key=my_key,  # Custom encryption key
    notification_topic=my_topic
)
```

A vault has a default `RemovalPolicy` set to `RETAIN`. Note that removing a vault
that contains recovery points will fail.

You can assign policies to backup vaults and the resources they contain. Assigning policies allows
you to do things like grant access to users to create backup plans and on-demand backups, but limit
their ability to delete recovery points after they're created.

Use the `accessPolicy` property to create a backup vault policy:

```python
vault = backup.BackupVault(self, "Vault",
    access_policy=iam.PolicyDocument(
        statements=[
            iam.PolicyStatement(
                effect=iam.Effect.DENY,
                principals=[iam.AnyPrincipal()],
                actions=["backup:DeleteRecoveryPoint"],
                resources=["*"],
                conditions={
                    "StringNotLike": {
                        "aws:userId": ["user1", "user2"
                        ]
                    }
                }
            )
        ]
    )
)
```

Alternativately statements can be added to the vault policy using `addToAccessPolicy()`.

Use the `blockRecoveryPointDeletion` property or the `blockRecoveryPointDeletion()` method to add
a statement to the vault access policy that prevents recovery point deletions in your vault:

```python
# backup_vault: backup.BackupVault
backup.BackupVault(self, "Vault",
    block_recovery_point_deletion=True
)
backup_vault.block_recovery_point_deletion()
```

By default access is not restricted.

## Importing existing backup vault

To import an existing backup vault into your CDK application, use the `BackupVault.fromBackupVaultArn` or `BackupVault.fromBackupVaultName`
static method. Here is an example of giving an IAM Role permission to start a backup job:

```python
imported_vault = backup.BackupVault.from_backup_vault_name(self, "Vault", "myVaultName")

role = iam.Role(self, "Access Role", assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"))

imported_vault.grant(role, "backup:StartBackupJob")
```
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk.aws_dynamodb as _aws_cdk_aws_dynamodb_eb1dc53b
import aws_cdk.aws_ec2 as _aws_cdk_aws_ec2_67de8e8d
import aws_cdk.aws_efs as _aws_cdk_aws_efs_b9f7a603
import aws_cdk.aws_events as _aws_cdk_aws_events_efcdfa54
import aws_cdk.aws_iam as _aws_cdk_aws_iam_940a1ce0
import aws_cdk.aws_kms as _aws_cdk_aws_kms_e491a92b
import aws_cdk.aws_rds as _aws_cdk_aws_rds_9543e6d5
import aws_cdk.aws_sns as _aws_cdk_aws_sns_889c7272
import aws_cdk.core as _aws_cdk_core_f4b25747
import constructs as _constructs_77d1e7e8


@jsii.data_type(
    jsii_type="@aws-cdk/aws-backup.BackupPlanProps",
    jsii_struct_bases=[],
    name_mapping={
        "backup_plan_name": "backupPlanName",
        "backup_plan_rules": "backupPlanRules",
        "backup_vault": "backupVault",
        "windows_vss": "windowsVss",
    },
)
class BackupPlanProps:
    def __init__(
        self,
        *,
        backup_plan_name: typing.Optional[builtins.str] = None,
        backup_plan_rules: typing.Optional[typing.Sequence["BackupPlanRule"]] = None,
        backup_vault: typing.Optional["IBackupVault"] = None,
        windows_vss: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Properties for a BackupPlan.

        :param backup_plan_name: The display name of the backup plan. Default: - A CDK generated name
        :param backup_plan_rules: Rules for the backup plan. Use ``addRule()`` to add rules after instantiation. Default: - use ``addRule()`` to add rules
        :param backup_vault: The backup vault where backups are stored. Default: - use the vault defined at the rule level. If not defined a new common vault for the plan will be created
        :param windows_vss: Enable Windows VSS backup. Default: false

        :exampleMetadata: infused

        Example::

            plan = backup.BackupPlan(self, "Plan",
                windows_vss=True
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2acb2eb5bc1d067554bdcdfd30b36e01da252db9b56958ab5733e505368517ee)
            check_type(argname="argument backup_plan_name", value=backup_plan_name, expected_type=type_hints["backup_plan_name"])
            check_type(argname="argument backup_plan_rules", value=backup_plan_rules, expected_type=type_hints["backup_plan_rules"])
            check_type(argname="argument backup_vault", value=backup_vault, expected_type=type_hints["backup_vault"])
            check_type(argname="argument windows_vss", value=windows_vss, expected_type=type_hints["windows_vss"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if backup_plan_name is not None:
            self._values["backup_plan_name"] = backup_plan_name
        if backup_plan_rules is not None:
            self._values["backup_plan_rules"] = backup_plan_rules
        if backup_vault is not None:
            self._values["backup_vault"] = backup_vault
        if windows_vss is not None:
            self._values["windows_vss"] = windows_vss

    @builtins.property
    def backup_plan_name(self) -> typing.Optional[builtins.str]:
        '''The display name of the backup plan.

        :default: - A CDK generated name
        '''
        result = self._values.get("backup_plan_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backup_plan_rules(self) -> typing.Optional[typing.List["BackupPlanRule"]]:
        '''Rules for the backup plan.

        Use ``addRule()`` to add rules after
        instantiation.

        :default: - use ``addRule()`` to add rules
        '''
        result = self._values.get("backup_plan_rules")
        return typing.cast(typing.Optional[typing.List["BackupPlanRule"]], result)

    @builtins.property
    def backup_vault(self) -> typing.Optional["IBackupVault"]:
        '''The backup vault where backups are stored.

        :default:

        - use the vault defined at the rule level. If not defined a new
        common vault for the plan will be created
        '''
        result = self._values.get("backup_vault")
        return typing.cast(typing.Optional["IBackupVault"], result)

    @builtins.property
    def windows_vss(self) -> typing.Optional[builtins.bool]:
        '''Enable Windows VSS backup.

        :default: false

        :see: https://docs.aws.amazon.com/aws-backup/latest/devguide/windows-backups.html
        '''
        result = self._values.get("windows_vss")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPlanProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BackupPlanRule(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-backup.BackupPlanRule",
):
    '''A backup plan rule.

    :exampleMetadata: infused

    Example::

        # plan: backup.BackupPlan
        
        plan.add_rule(backup.BackupPlanRule.daily())
        plan.add_rule(backup.BackupPlanRule.weekly())
    '''

    def __init__(
        self,
        *,
        backup_vault: typing.Optional["IBackupVault"] = None,
        completion_window: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        delete_after: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        enable_continuous_backup: typing.Optional[builtins.bool] = None,
        move_to_cold_storage_after: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        rule_name: typing.Optional[builtins.str] = None,
        schedule_expression: typing.Optional[_aws_cdk_aws_events_efcdfa54.Schedule] = None,
        start_window: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    ) -> None:
        '''
        :param backup_vault: The backup vault where backups are. Default: - use the vault defined at the plan level. If not defined a new common vault for the plan will be created
        :param completion_window: The duration after a backup job is successfully started before it must be completed or it is canceled by AWS Backup. Default: - 8 hours
        :param delete_after: Specifies the duration after creation that a recovery point is deleted. Must be greater than ``moveToColdStorageAfter``. Default: - recovery point is never deleted
        :param enable_continuous_backup: Enables continuous backup and point-in-time restores (PITR). Property ``deleteAfter`` defines the retention period for the backup. It is mandatory if PITR is enabled. If no value is specified, the retention period is set to 35 days which is the maximum retention period supported by PITR. Property ``moveToColdStorageAfter`` must not be specified because PITR does not support this option. Default: false
        :param move_to_cold_storage_after: Specifies the duration after creation that a recovery point is moved to cold storage. Default: - recovery point is never moved to cold storage
        :param rule_name: A display name for the backup rule. Default: - a CDK generated name
        :param schedule_expression: A CRON expression specifying when AWS Backup initiates a backup job. Default: - no schedule
        :param start_window: The duration after a backup is scheduled before a job is canceled if it doesn't start successfully. Default: - 8 hours
        '''
        props = BackupPlanRuleProps(
            backup_vault=backup_vault,
            completion_window=completion_window,
            delete_after=delete_after,
            enable_continuous_backup=enable_continuous_backup,
            move_to_cold_storage_after=move_to_cold_storage_after,
            rule_name=rule_name,
            schedule_expression=schedule_expression,
            start_window=start_window,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="daily")
    @builtins.classmethod
    def daily(
        cls,
        backup_vault: typing.Optional["IBackupVault"] = None,
    ) -> "BackupPlanRule":
        '''Daily with 35 days retention.

        :param backup_vault: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f110a430335c0a2cadc6c66c132b0ea5d3fe0627f04ad81b4654afc1373b8e5)
            check_type(argname="argument backup_vault", value=backup_vault, expected_type=type_hints["backup_vault"])
        return typing.cast("BackupPlanRule", jsii.sinvoke(cls, "daily", [backup_vault]))

    @jsii.member(jsii_name="monthly1Year")
    @builtins.classmethod
    def monthly1_year(
        cls,
        backup_vault: typing.Optional["IBackupVault"] = None,
    ) -> "BackupPlanRule":
        '''Monthly 1 year retention, move to cold storage after 1 month.

        :param backup_vault: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c15208867c69a473d2e6a7c205c515634fd975057410c281b40435913774f65)
            check_type(argname="argument backup_vault", value=backup_vault, expected_type=type_hints["backup_vault"])
        return typing.cast("BackupPlanRule", jsii.sinvoke(cls, "monthly1Year", [backup_vault]))

    @jsii.member(jsii_name="monthly5Year")
    @builtins.classmethod
    def monthly5_year(
        cls,
        backup_vault: typing.Optional["IBackupVault"] = None,
    ) -> "BackupPlanRule":
        '''Monthly 5 year retention, move to cold storage after 3 months.

        :param backup_vault: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f38dbcdb3654b77cf7b041c4d0e1dd9372bca7757d2dc0b562932abcbdfde510)
            check_type(argname="argument backup_vault", value=backup_vault, expected_type=type_hints["backup_vault"])
        return typing.cast("BackupPlanRule", jsii.sinvoke(cls, "monthly5Year", [backup_vault]))

    @jsii.member(jsii_name="monthly7Year")
    @builtins.classmethod
    def monthly7_year(
        cls,
        backup_vault: typing.Optional["IBackupVault"] = None,
    ) -> "BackupPlanRule":
        '''Monthly 7 year retention, move to cold storage after 3 months.

        :param backup_vault: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52b6de1b57ab1725c4b3debdf9f46c0022dcc6bc0fb70e9dc5d6c7d6a3e9bd5d)
            check_type(argname="argument backup_vault", value=backup_vault, expected_type=type_hints["backup_vault"])
        return typing.cast("BackupPlanRule", jsii.sinvoke(cls, "monthly7Year", [backup_vault]))

    @jsii.member(jsii_name="weekly")
    @builtins.classmethod
    def weekly(
        cls,
        backup_vault: typing.Optional["IBackupVault"] = None,
    ) -> "BackupPlanRule":
        '''Weekly with 3 months retention.

        :param backup_vault: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89d9135477decffd88cfe7297a0c68b34a8c1dc82c2de311099b66aa31c8c870)
            check_type(argname="argument backup_vault", value=backup_vault, expected_type=type_hints["backup_vault"])
        return typing.cast("BackupPlanRule", jsii.sinvoke(cls, "weekly", [backup_vault]))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "BackupPlanRuleProps":
        '''Properties of BackupPlanRule.'''
        return typing.cast("BackupPlanRuleProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-backup.BackupPlanRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "backup_vault": "backupVault",
        "completion_window": "completionWindow",
        "delete_after": "deleteAfter",
        "enable_continuous_backup": "enableContinuousBackup",
        "move_to_cold_storage_after": "moveToColdStorageAfter",
        "rule_name": "ruleName",
        "schedule_expression": "scheduleExpression",
        "start_window": "startWindow",
    },
)
class BackupPlanRuleProps:
    def __init__(
        self,
        *,
        backup_vault: typing.Optional["IBackupVault"] = None,
        completion_window: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        delete_after: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        enable_continuous_backup: typing.Optional[builtins.bool] = None,
        move_to_cold_storage_after: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        rule_name: typing.Optional[builtins.str] = None,
        schedule_expression: typing.Optional[_aws_cdk_aws_events_efcdfa54.Schedule] = None,
        start_window: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    ) -> None:
        '''Properties for a BackupPlanRule.

        :param backup_vault: The backup vault where backups are. Default: - use the vault defined at the plan level. If not defined a new common vault for the plan will be created
        :param completion_window: The duration after a backup job is successfully started before it must be completed or it is canceled by AWS Backup. Default: - 8 hours
        :param delete_after: Specifies the duration after creation that a recovery point is deleted. Must be greater than ``moveToColdStorageAfter``. Default: - recovery point is never deleted
        :param enable_continuous_backup: Enables continuous backup and point-in-time restores (PITR). Property ``deleteAfter`` defines the retention period for the backup. It is mandatory if PITR is enabled. If no value is specified, the retention period is set to 35 days which is the maximum retention period supported by PITR. Property ``moveToColdStorageAfter`` must not be specified because PITR does not support this option. Default: false
        :param move_to_cold_storage_after: Specifies the duration after creation that a recovery point is moved to cold storage. Default: - recovery point is never moved to cold storage
        :param rule_name: A display name for the backup rule. Default: - a CDK generated name
        :param schedule_expression: A CRON expression specifying when AWS Backup initiates a backup job. Default: - no schedule
        :param start_window: The duration after a backup is scheduled before a job is canceled if it doesn't start successfully. Default: - 8 hours

        :exampleMetadata: infused

        Example::

            # plan: backup.BackupPlan
            
            plan.add_rule(backup.BackupPlanRule(
                completion_window=Duration.hours(2),
                start_window=Duration.hours(1),
                schedule_expression=events.Schedule.cron( # Only cron expressions are supported
                    day="15",
                    hour="3",
                    minute="30"),
                move_to_cold_storage_after=Duration.days(30)
            ))
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89d1d01ed5709cfaad4c388e5791c6f275749bc559482d6625a5b9f232b804e2)
            check_type(argname="argument backup_vault", value=backup_vault, expected_type=type_hints["backup_vault"])
            check_type(argname="argument completion_window", value=completion_window, expected_type=type_hints["completion_window"])
            check_type(argname="argument delete_after", value=delete_after, expected_type=type_hints["delete_after"])
            check_type(argname="argument enable_continuous_backup", value=enable_continuous_backup, expected_type=type_hints["enable_continuous_backup"])
            check_type(argname="argument move_to_cold_storage_after", value=move_to_cold_storage_after, expected_type=type_hints["move_to_cold_storage_after"])
            check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
            check_type(argname="argument schedule_expression", value=schedule_expression, expected_type=type_hints["schedule_expression"])
            check_type(argname="argument start_window", value=start_window, expected_type=type_hints["start_window"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if backup_vault is not None:
            self._values["backup_vault"] = backup_vault
        if completion_window is not None:
            self._values["completion_window"] = completion_window
        if delete_after is not None:
            self._values["delete_after"] = delete_after
        if enable_continuous_backup is not None:
            self._values["enable_continuous_backup"] = enable_continuous_backup
        if move_to_cold_storage_after is not None:
            self._values["move_to_cold_storage_after"] = move_to_cold_storage_after
        if rule_name is not None:
            self._values["rule_name"] = rule_name
        if schedule_expression is not None:
            self._values["schedule_expression"] = schedule_expression
        if start_window is not None:
            self._values["start_window"] = start_window

    @builtins.property
    def backup_vault(self) -> typing.Optional["IBackupVault"]:
        '''The backup vault where backups are.

        :default:

        - use the vault defined at the plan level. If not defined a new
        common vault for the plan will be created
        '''
        result = self._values.get("backup_vault")
        return typing.cast(typing.Optional["IBackupVault"], result)

    @builtins.property
    def completion_window(self) -> typing.Optional[_aws_cdk_core_f4b25747.Duration]:
        '''The duration after a backup job is successfully started before it must be completed or it is canceled by AWS Backup.

        :default: - 8 hours
        '''
        result = self._values.get("completion_window")
        return typing.cast(typing.Optional[_aws_cdk_core_f4b25747.Duration], result)

    @builtins.property
    def delete_after(self) -> typing.Optional[_aws_cdk_core_f4b25747.Duration]:
        '''Specifies the duration after creation that a recovery point is deleted.

        Must be greater than ``moveToColdStorageAfter``.

        :default: - recovery point is never deleted
        '''
        result = self._values.get("delete_after")
        return typing.cast(typing.Optional[_aws_cdk_core_f4b25747.Duration], result)

    @builtins.property
    def enable_continuous_backup(self) -> typing.Optional[builtins.bool]:
        '''Enables continuous backup and point-in-time restores (PITR).

        Property ``deleteAfter`` defines the retention period for the backup. It is mandatory if PITR is enabled.
        If no value is specified, the retention period is set to 35 days which is the maximum retention period supported by PITR.

        Property ``moveToColdStorageAfter`` must not be specified because PITR does not support this option.

        :default: false
        '''
        result = self._values.get("enable_continuous_backup")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def move_to_cold_storage_after(
        self,
    ) -> typing.Optional[_aws_cdk_core_f4b25747.Duration]:
        '''Specifies the duration after creation that a recovery point is moved to cold storage.

        :default: - recovery point is never moved to cold storage
        '''
        result = self._values.get("move_to_cold_storage_after")
        return typing.cast(typing.Optional[_aws_cdk_core_f4b25747.Duration], result)

    @builtins.property
    def rule_name(self) -> typing.Optional[builtins.str]:
        '''A display name for the backup rule.

        :default: - a CDK generated name
        '''
        result = self._values.get("rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule_expression(
        self,
    ) -> typing.Optional[_aws_cdk_aws_events_efcdfa54.Schedule]:
        '''A CRON expression specifying when AWS Backup initiates a backup job.

        :default: - no schedule
        '''
        result = self._values.get("schedule_expression")
        return typing.cast(typing.Optional[_aws_cdk_aws_events_efcdfa54.Schedule], result)

    @builtins.property
    def start_window(self) -> typing.Optional[_aws_cdk_core_f4b25747.Duration]:
        '''The duration after a backup is scheduled before a job is canceled if it doesn't start successfully.

        :default: - 8 hours
        '''
        result = self._values.get("start_window")
        return typing.cast(typing.Optional[_aws_cdk_core_f4b25747.Duration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPlanRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BackupResource(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-backup.BackupResource",
):
    '''A resource to backup.

    :exampleMetadata: infused

    Example::

        # plan: backup.BackupPlan
        
        my_table = dynamodb.Table.from_table_name(self, "Table", "myTableName")
        my_cool_construct = Construct(self, "MyCoolConstruct")
        
        plan.add_selection("Selection",
            resources=[
                backup.BackupResource.from_dynamo_db_table(my_table),  # A DynamoDB table
                backup.BackupResource.from_tag("stage", "prod"),  # All resources that are tagged stage=prod in the region/account
                backup.BackupResource.from_construct(my_cool_construct)
            ]
        )
    '''

    def __init__(
        self,
        resource: typing.Optional[builtins.str] = None,
        tag_condition: typing.Optional[typing.Union["TagCondition", typing.Dict[builtins.str, typing.Any]]] = None,
        construct: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    ) -> None:
        '''
        :param resource: -
        :param tag_condition: -
        :param construct: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9511c787f66a3b400ce49c7e9ace7abf3b5bdaf73c953eb33459c1a46da83c7e)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument tag_condition", value=tag_condition, expected_type=type_hints["tag_condition"])
            check_type(argname="argument construct", value=construct, expected_type=type_hints["construct"])
        jsii.create(self.__class__, self, [resource, tag_condition, construct])

    @jsii.member(jsii_name="fromArn")
    @builtins.classmethod
    def from_arn(cls, arn: builtins.str) -> "BackupResource":
        '''A list of ARNs or match patterns such as ``arn:aws:ec2:us-east-1:123456789012:volume/*``.

        :param arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdc90484c5f31d5acb6c903fe40f5017bff83ca657b2f8ad6a45d525c864b32b)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        return typing.cast("BackupResource", jsii.sinvoke(cls, "fromArn", [arn]))

    @jsii.member(jsii_name="fromConstruct")
    @builtins.classmethod
    def from_construct(
        cls,
        construct: _constructs_77d1e7e8.Construct,
    ) -> "BackupResource":
        '''Adds all supported resources in a construct.

        :param construct: The construct containing resources to backup.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d5274e11558a710a6465c4efc73c5940461b76f7c38973085611d292e66e265)
            check_type(argname="argument construct", value=construct, expected_type=type_hints["construct"])
        return typing.cast("BackupResource", jsii.sinvoke(cls, "fromConstruct", [construct]))

    @jsii.member(jsii_name="fromDynamoDbTable")
    @builtins.classmethod
    def from_dynamo_db_table(
        cls,
        table: _aws_cdk_aws_dynamodb_eb1dc53b.ITable,
    ) -> "BackupResource":
        '''A DynamoDB table.

        :param table: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efe968d8d893061c9b2e4ae72464c31535d419b940944207c36f78b5db9221ed)
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
        return typing.cast("BackupResource", jsii.sinvoke(cls, "fromDynamoDbTable", [table]))

    @jsii.member(jsii_name="fromEc2Instance")
    @builtins.classmethod
    def from_ec2_instance(
        cls,
        instance: _aws_cdk_aws_ec2_67de8e8d.IInstance,
    ) -> "BackupResource":
        '''An EC2 instance.

        :param instance: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__438c3d8ec4e566e8bfd10a9463a8c497ae9a57884808b114410593e9677923bb)
            check_type(argname="argument instance", value=instance, expected_type=type_hints["instance"])
        return typing.cast("BackupResource", jsii.sinvoke(cls, "fromEc2Instance", [instance]))

    @jsii.member(jsii_name="fromEfsFileSystem")
    @builtins.classmethod
    def from_efs_file_system(
        cls,
        file_system: _aws_cdk_aws_efs_b9f7a603.IFileSystem,
    ) -> "BackupResource":
        '''An EFS file system.

        :param file_system: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c082fb5a6093279f9e88aade9235e065c2088f8417f2bc12a0dca57fd72366ff)
            check_type(argname="argument file_system", value=file_system, expected_type=type_hints["file_system"])
        return typing.cast("BackupResource", jsii.sinvoke(cls, "fromEfsFileSystem", [file_system]))

    @jsii.member(jsii_name="fromRdsDatabaseInstance")
    @builtins.classmethod
    def from_rds_database_instance(
        cls,
        instance: _aws_cdk_aws_rds_9543e6d5.IDatabaseInstance,
    ) -> "BackupResource":
        '''A RDS database instance.

        :param instance: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a97d5f6f97ce4a5882ec214ed68c59fac955d7f55a5c8c4bb4c283d8e50b1cf)
            check_type(argname="argument instance", value=instance, expected_type=type_hints["instance"])
        return typing.cast("BackupResource", jsii.sinvoke(cls, "fromRdsDatabaseInstance", [instance]))

    @jsii.member(jsii_name="fromTag")
    @builtins.classmethod
    def from_tag(
        cls,
        key: builtins.str,
        value: builtins.str,
        operation: typing.Optional["TagOperation"] = None,
    ) -> "BackupResource":
        '''A tag condition.

        :param key: -
        :param value: -
        :param operation: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c339f15ec1fce1f739dcb83a56674fa9490f08ad4709bb733a17d3490829a9d)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument operation", value=operation, expected_type=type_hints["operation"])
        return typing.cast("BackupResource", jsii.sinvoke(cls, "fromTag", [key, value, operation]))

    @builtins.property
    @jsii.member(jsii_name="construct")
    def construct(self) -> typing.Optional[_aws_cdk_core_f4b25747.Construct]:
        '''A construct.'''
        return typing.cast(typing.Optional[_aws_cdk_core_f4b25747.Construct], jsii.get(self, "construct"))

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> typing.Optional[builtins.str]:
        '''A resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resource"))

    @builtins.property
    @jsii.member(jsii_name="tagCondition")
    def tag_condition(self) -> typing.Optional["TagCondition"]:
        '''A condition on a tag.'''
        return typing.cast(typing.Optional["TagCondition"], jsii.get(self, "tagCondition"))


@jsii.implements(_aws_cdk_aws_iam_940a1ce0.IGrantable)
class BackupSelection(
    _aws_cdk_core_f4b25747.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-backup.BackupSelection",
):
    '''A backup selection.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_backup as backup
        import aws_cdk.aws_iam as iam
        
        # backup_plan: backup.BackupPlan
        # backup_resource: backup.BackupResource
        # role: iam.Role
        
        backup_selection = backup.BackupSelection(self, "MyBackupSelection",
            backup_plan=backup_plan,
            resources=[backup_resource],
        
            # the properties below are optional
            allow_restores=False,
            backup_selection_name="backupSelectionName",
            role=role
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        backup_plan: "IBackupPlan",
        resources: typing.Sequence[BackupResource],
        allow_restores: typing.Optional[builtins.bool] = None,
        backup_selection_name: typing.Optional[builtins.str] = None,
        role: typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param backup_plan: The backup plan for this selection.
        :param resources: The resources to backup. Use the helper static methods defined on ``BackupResource``.
        :param allow_restores: Whether to automatically give restores permissions to the role that AWS Backup uses. If ``true``, the ``AWSBackupServiceRolePolicyForRestores`` managed policy will be attached to the role. Default: false
        :param backup_selection_name: The name for this selection. Default: - a CDK generated name
        :param role: The role that AWS Backup uses to authenticate when backuping or restoring the resources. The ``AWSBackupServiceRolePolicyForBackup`` managed policy will be attached to this role. Default: - a new role will be created
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dea399d8b73419df7fd11794674ce6a592c2f288198d53ac7e19679fa349a7a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = BackupSelectionProps(
            backup_plan=backup_plan,
            resources=resources,
            allow_restores=allow_restores,
            backup_selection_name=backup_selection_name,
            role=role,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="backupPlanId")
    def backup_plan_id(self) -> builtins.str:
        '''The identifier of the backup plan.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "backupPlanId"))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> _aws_cdk_aws_iam_940a1ce0.IPrincipal:
        '''The principal to grant permissions to.'''
        return typing.cast(_aws_cdk_aws_iam_940a1ce0.IPrincipal, jsii.get(self, "grantPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="selectionId")
    def selection_id(self) -> builtins.str:
        '''The identifier of the backup selection.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "selectionId"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-backup.BackupSelectionOptions",
    jsii_struct_bases=[],
    name_mapping={
        "resources": "resources",
        "allow_restores": "allowRestores",
        "backup_selection_name": "backupSelectionName",
        "role": "role",
    },
)
class BackupSelectionOptions:
    def __init__(
        self,
        *,
        resources: typing.Sequence[BackupResource],
        allow_restores: typing.Optional[builtins.bool] = None,
        backup_selection_name: typing.Optional[builtins.str] = None,
        role: typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole] = None,
    ) -> None:
        '''Options for a BackupSelection.

        :param resources: The resources to backup. Use the helper static methods defined on ``BackupResource``.
        :param allow_restores: Whether to automatically give restores permissions to the role that AWS Backup uses. If ``true``, the ``AWSBackupServiceRolePolicyForRestores`` managed policy will be attached to the role. Default: false
        :param backup_selection_name: The name for this selection. Default: - a CDK generated name
        :param role: The role that AWS Backup uses to authenticate when backuping or restoring the resources. The ``AWSBackupServiceRolePolicyForBackup`` managed policy will be attached to this role. Default: - a new role will be created

        :exampleMetadata: infused

        Example::

            # plan: backup.BackupPlan
            
            my_table = dynamodb.Table.from_table_name(self, "Table", "myTableName")
            my_cool_construct = Construct(self, "MyCoolConstruct")
            
            plan.add_selection("Selection",
                resources=[
                    backup.BackupResource.from_dynamo_db_table(my_table),  # A DynamoDB table
                    backup.BackupResource.from_tag("stage", "prod"),  # All resources that are tagged stage=prod in the region/account
                    backup.BackupResource.from_construct(my_cool_construct)
                ]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b88c60fb1713ec923f2ac9c23d30eb8b6b44ff2a99fe03094647b5cdfba2a3b)
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument allow_restores", value=allow_restores, expected_type=type_hints["allow_restores"])
            check_type(argname="argument backup_selection_name", value=backup_selection_name, expected_type=type_hints["backup_selection_name"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resources": resources,
        }
        if allow_restores is not None:
            self._values["allow_restores"] = allow_restores
        if backup_selection_name is not None:
            self._values["backup_selection_name"] = backup_selection_name
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def resources(self) -> typing.List[BackupResource]:
        '''The resources to backup.

        Use the helper static methods defined on ``BackupResource``.
        '''
        result = self._values.get("resources")
        assert result is not None, "Required property 'resources' is missing"
        return typing.cast(typing.List[BackupResource], result)

    @builtins.property
    def allow_restores(self) -> typing.Optional[builtins.bool]:
        '''Whether to automatically give restores permissions to the role that AWS Backup uses.

        If ``true``, the ``AWSBackupServiceRolePolicyForRestores`` managed
        policy will be attached to the role.

        :default: false
        '''
        result = self._values.get("allow_restores")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def backup_selection_name(self) -> typing.Optional[builtins.str]:
        '''The name for this selection.

        :default: - a CDK generated name
        '''
        result = self._values.get("backup_selection_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole]:
        '''The role that AWS Backup uses to authenticate when backuping or restoring the resources.

        The ``AWSBackupServiceRolePolicyForBackup`` managed policy
        will be attached to this role.

        :default: - a new role will be created
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupSelectionOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-backup.BackupSelectionProps",
    jsii_struct_bases=[BackupSelectionOptions],
    name_mapping={
        "resources": "resources",
        "allow_restores": "allowRestores",
        "backup_selection_name": "backupSelectionName",
        "role": "role",
        "backup_plan": "backupPlan",
    },
)
class BackupSelectionProps(BackupSelectionOptions):
    def __init__(
        self,
        *,
        resources: typing.Sequence[BackupResource],
        allow_restores: typing.Optional[builtins.bool] = None,
        backup_selection_name: typing.Optional[builtins.str] = None,
        role: typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole] = None,
        backup_plan: "IBackupPlan",
    ) -> None:
        '''Properties for a BackupSelection.

        :param resources: The resources to backup. Use the helper static methods defined on ``BackupResource``.
        :param allow_restores: Whether to automatically give restores permissions to the role that AWS Backup uses. If ``true``, the ``AWSBackupServiceRolePolicyForRestores`` managed policy will be attached to the role. Default: false
        :param backup_selection_name: The name for this selection. Default: - a CDK generated name
        :param role: The role that AWS Backup uses to authenticate when backuping or restoring the resources. The ``AWSBackupServiceRolePolicyForBackup`` managed policy will be attached to this role. Default: - a new role will be created
        :param backup_plan: The backup plan for this selection.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_backup as backup
            import aws_cdk.aws_iam as iam
            
            # backup_plan: backup.BackupPlan
            # backup_resource: backup.BackupResource
            # role: iam.Role
            
            backup_selection_props = backup.BackupSelectionProps(
                backup_plan=backup_plan,
                resources=[backup_resource],
            
                # the properties below are optional
                allow_restores=False,
                backup_selection_name="backupSelectionName",
                role=role
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e70b1c7baf6a9648962e10d5080a92d126a38007360f96266e015c655874b03)
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument allow_restores", value=allow_restores, expected_type=type_hints["allow_restores"])
            check_type(argname="argument backup_selection_name", value=backup_selection_name, expected_type=type_hints["backup_selection_name"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument backup_plan", value=backup_plan, expected_type=type_hints["backup_plan"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resources": resources,
            "backup_plan": backup_plan,
        }
        if allow_restores is not None:
            self._values["allow_restores"] = allow_restores
        if backup_selection_name is not None:
            self._values["backup_selection_name"] = backup_selection_name
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def resources(self) -> typing.List[BackupResource]:
        '''The resources to backup.

        Use the helper static methods defined on ``BackupResource``.
        '''
        result = self._values.get("resources")
        assert result is not None, "Required property 'resources' is missing"
        return typing.cast(typing.List[BackupResource], result)

    @builtins.property
    def allow_restores(self) -> typing.Optional[builtins.bool]:
        '''Whether to automatically give restores permissions to the role that AWS Backup uses.

        If ``true``, the ``AWSBackupServiceRolePolicyForRestores`` managed
        policy will be attached to the role.

        :default: false
        '''
        result = self._values.get("allow_restores")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def backup_selection_name(self) -> typing.Optional[builtins.str]:
        '''The name for this selection.

        :default: - a CDK generated name
        '''
        result = self._values.get("backup_selection_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole]:
        '''The role that AWS Backup uses to authenticate when backuping or restoring the resources.

        The ``AWSBackupServiceRolePolicyForBackup`` managed policy
        will be attached to this role.

        :default: - a new role will be created
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole], result)

    @builtins.property
    def backup_plan(self) -> "IBackupPlan":
        '''The backup plan for this selection.'''
        result = self._values.get("backup_plan")
        assert result is not None, "Required property 'backup_plan' is missing"
        return typing.cast("IBackupPlan", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupSelectionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/aws-backup.BackupVaultEvents")
class BackupVaultEvents(enum.Enum):
    '''Backup vault events.'''

    BACKUP_JOB_STARTED = "BACKUP_JOB_STARTED"
    '''BACKUP_JOB_STARTED.'''
    BACKUP_JOB_COMPLETED = "BACKUP_JOB_COMPLETED"
    '''BACKUP_JOB_COMPLETED.'''
    BACKUP_JOB_SUCCESSFUL = "BACKUP_JOB_SUCCESSFUL"
    '''BACKUP_JOB_SUCCESSFUL.'''
    BACKUP_JOB_FAILED = "BACKUP_JOB_FAILED"
    '''BACKUP_JOB_FAILED.'''
    BACKUP_JOB_EXPIRED = "BACKUP_JOB_EXPIRED"
    '''BACKUP_JOB_EXPIRED.'''
    RESTORE_JOB_STARTED = "RESTORE_JOB_STARTED"
    '''RESTORE_JOB_STARTED.'''
    RESTORE_JOB_COMPLETED = "RESTORE_JOB_COMPLETED"
    '''RESTORE_JOB_COMPLETED.'''
    RESTORE_JOB_SUCCESSFUL = "RESTORE_JOB_SUCCESSFUL"
    '''RESTORE_JOB_SUCCESSFUL.'''
    RESTORE_JOB_FAILED = "RESTORE_JOB_FAILED"
    '''RESTORE_JOB_FAILED.'''
    COPY_JOB_STARTED = "COPY_JOB_STARTED"
    '''COPY_JOB_STARTED.'''
    COPY_JOB_SUCCESSFUL = "COPY_JOB_SUCCESSFUL"
    '''COPY_JOB_SUCCESSFUL.'''
    COPY_JOB_FAILED = "COPY_JOB_FAILED"
    '''COPY_JOB_FAILED.'''
    RECOVERY_POINT_MODIFIED = "RECOVERY_POINT_MODIFIED"
    '''RECOVERY_POINT_MODIFIED.'''
    BACKUP_PLAN_CREATED = "BACKUP_PLAN_CREATED"
    '''BACKUP_PLAN_CREATED.'''
    BACKUP_PLAN_MODIFIED = "BACKUP_PLAN_MODIFIED"
    '''BACKUP_PLAN_MODIFIED.'''


@jsii.data_type(
    jsii_type="@aws-cdk/aws-backup.BackupVaultProps",
    jsii_struct_bases=[],
    name_mapping={
        "access_policy": "accessPolicy",
        "backup_vault_name": "backupVaultName",
        "block_recovery_point_deletion": "blockRecoveryPointDeletion",
        "encryption_key": "encryptionKey",
        "notification_events": "notificationEvents",
        "notification_topic": "notificationTopic",
        "removal_policy": "removalPolicy",
    },
)
class BackupVaultProps:
    def __init__(
        self,
        *,
        access_policy: typing.Optional[_aws_cdk_aws_iam_940a1ce0.PolicyDocument] = None,
        backup_vault_name: typing.Optional[builtins.str] = None,
        block_recovery_point_deletion: typing.Optional[builtins.bool] = None,
        encryption_key: typing.Optional[_aws_cdk_aws_kms_e491a92b.IKey] = None,
        notification_events: typing.Optional[typing.Sequence[BackupVaultEvents]] = None,
        notification_topic: typing.Optional[_aws_cdk_aws_sns_889c7272.ITopic] = None,
        removal_policy: typing.Optional[_aws_cdk_core_f4b25747.RemovalPolicy] = None,
    ) -> None:
        '''Properties for a BackupVault.

        :param access_policy: A resource-based policy that is used to manage access permissions on the backup vault. Default: - access is not restricted
        :param backup_vault_name: The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. Default: - A CDK generated name
        :param block_recovery_point_deletion: Whether to add statements to the vault access policy that prevents anyone from deleting a recovery point. Default: false
        :param encryption_key: The server-side encryption key to use to protect your backups. Default: - an Amazon managed KMS key
        :param notification_events: The vault events to send. Default: - all vault events if ``notificationTopic`` is defined
        :param notification_topic: A SNS topic to send vault events to. Default: - no notifications
        :param removal_policy: The removal policy to apply to the vault. Note that removing a vault that contains recovery points will fail. Default: RemovalPolicy.RETAIN

        :exampleMetadata: infused

        Example::

            my_key = kms.Key.from_key_arn(self, "MyKey", "aaa")
            my_topic = sns.Topic.from_topic_arn(self, "MyTopic", "bbb")
            
            vault = backup.BackupVault(self, "Vault",
                encryption_key=my_key,  # Custom encryption key
                notification_topic=my_topic
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ac441c7052b5e06554cd46a9f3d909913e6d4bfd680be32296a58b3ededaf32)
            check_type(argname="argument access_policy", value=access_policy, expected_type=type_hints["access_policy"])
            check_type(argname="argument backup_vault_name", value=backup_vault_name, expected_type=type_hints["backup_vault_name"])
            check_type(argname="argument block_recovery_point_deletion", value=block_recovery_point_deletion, expected_type=type_hints["block_recovery_point_deletion"])
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            check_type(argname="argument notification_events", value=notification_events, expected_type=type_hints["notification_events"])
            check_type(argname="argument notification_topic", value=notification_topic, expected_type=type_hints["notification_topic"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_policy is not None:
            self._values["access_policy"] = access_policy
        if backup_vault_name is not None:
            self._values["backup_vault_name"] = backup_vault_name
        if block_recovery_point_deletion is not None:
            self._values["block_recovery_point_deletion"] = block_recovery_point_deletion
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if notification_events is not None:
            self._values["notification_events"] = notification_events
        if notification_topic is not None:
            self._values["notification_topic"] = notification_topic
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy

    @builtins.property
    def access_policy(
        self,
    ) -> typing.Optional[_aws_cdk_aws_iam_940a1ce0.PolicyDocument]:
        '''A resource-based policy that is used to manage access permissions on the backup vault.

        :default: - access is not restricted
        '''
        result = self._values.get("access_policy")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_940a1ce0.PolicyDocument], result)

    @builtins.property
    def backup_vault_name(self) -> typing.Optional[builtins.str]:
        '''The name of a logical container where backups are stored.

        Backup vaults
        are identified by names that are unique to the account used to create
        them and the AWS Region where they are created.

        :default: - A CDK generated name
        '''
        result = self._values.get("backup_vault_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def block_recovery_point_deletion(self) -> typing.Optional[builtins.bool]:
        '''Whether to add statements to the vault access policy that prevents anyone from deleting a recovery point.

        :default: false
        '''
        result = self._values.get("block_recovery_point_deletion")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[_aws_cdk_aws_kms_e491a92b.IKey]:
        '''The server-side encryption key to use to protect your backups.

        :default: - an Amazon managed KMS key
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[_aws_cdk_aws_kms_e491a92b.IKey], result)

    @builtins.property
    def notification_events(self) -> typing.Optional[typing.List[BackupVaultEvents]]:
        '''The vault events to send.

        :default: - all vault events if ``notificationTopic`` is defined

        :see: https://docs.aws.amazon.com/aws-backup/latest/devguide/sns-notifications.html
        '''
        result = self._values.get("notification_events")
        return typing.cast(typing.Optional[typing.List[BackupVaultEvents]], result)

    @builtins.property
    def notification_topic(self) -> typing.Optional[_aws_cdk_aws_sns_889c7272.ITopic]:
        '''A SNS topic to send vault events to.

        :default: - no notifications

        :see: https://docs.aws.amazon.com/aws-backup/latest/devguide/sns-notifications.html
        '''
        result = self._values.get("notification_topic")
        return typing.cast(typing.Optional[_aws_cdk_aws_sns_889c7272.ITopic], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_aws_cdk_core_f4b25747.RemovalPolicy]:
        '''The removal policy to apply to the vault.

        Note that removing a vault
        that contains recovery points will fail.

        :default: RemovalPolicy.RETAIN
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_aws_cdk_core_f4b25747.RemovalPolicy], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupVaultProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnBackupPlan(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-backup.CfnBackupPlan",
):
    '''A CloudFormation ``AWS::Backup::BackupPlan``.

    Contains an optional backup plan display name and an array of ``BackupRule`` objects, each of which specifies a backup rule. Each rule in a backup plan is a separate scheduled task and can back up a different selection of AWS resources.

    For a sample AWS CloudFormation template, see the `AWS Backup Developer Guide <https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html#assigning-resources-cfn>`_ .

    :cloudformationResource: AWS::Backup::BackupPlan
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_backup as backup
        
        # backup_options: Any
        
        cfn_backup_plan = backup.CfnBackupPlan(self, "MyCfnBackupPlan",
            backup_plan=backup.CfnBackupPlan.BackupPlanResourceTypeProperty(
                backup_plan_name="backupPlanName",
                backup_plan_rule=[backup.CfnBackupPlan.BackupRuleResourceTypeProperty(
                    rule_name="ruleName",
                    target_backup_vault="targetBackupVault",
        
                    # the properties below are optional
                    completion_window_minutes=123,
                    copy_actions=[backup.CfnBackupPlan.CopyActionResourceTypeProperty(
                        destination_backup_vault_arn="destinationBackupVaultArn",
        
                        # the properties below are optional
                        lifecycle=backup.CfnBackupPlan.LifecycleResourceTypeProperty(
                            delete_after_days=123,
                            move_to_cold_storage_after_days=123
                        )
                    )],
                    enable_continuous_backup=False,
                    lifecycle=backup.CfnBackupPlan.LifecycleResourceTypeProperty(
                        delete_after_days=123,
                        move_to_cold_storage_after_days=123
                    ),
                    recovery_point_tags={
                        "recovery_point_tags_key": "recoveryPointTags"
                    },
                    schedule_expression="scheduleExpression",
                    start_window_minutes=123
                )],
        
                # the properties below are optional
                advanced_backup_settings=[backup.CfnBackupPlan.AdvancedBackupSettingResourceTypeProperty(
                    backup_options=backup_options,
                    resource_type="resourceType"
                )]
            ),
        
            # the properties below are optional
            backup_plan_tags={
                "backup_plan_tags_key": "backupPlanTags"
            }
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        backup_plan: typing.Union[typing.Union["CfnBackupPlan.BackupPlanResourceTypeProperty", typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable],
        backup_plan_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
    ) -> None:
        '''Create a new ``AWS::Backup::BackupPlan``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param backup_plan: Uniquely identifies the backup plan to be associated with the selection of resources.
        :param backup_plan_tags: To help organize your resources, you can assign your own metadata to the resources that you create. Each tag is a key-value pair. The specified tags are assigned to all backups created with this plan.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b22513aceab736628f16f83e016a1e02a13f944c473f991529098b89737d72a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBackupPlanProps(
            backup_plan=backup_plan, backup_plan_tags=backup_plan_tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a79e7ff0cfd5897d3704cab22d1908eb137f61444e7af9ce43223e52022b9352)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11e6584ce5574bd36e64401d7b12be835d7a54af655365835553a75450196a69)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrBackupPlanArn")
    def attr_backup_plan_arn(self) -> builtins.str:
        '''An Amazon Resource Name (ARN) that uniquely identifies a backup plan;

        for example, ``arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`` .

        :cloudformationAttribute: BackupPlanArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBackupPlanArn"))

    @builtins.property
    @jsii.member(jsii_name="attrBackupPlanId")
    def attr_backup_plan_id(self) -> builtins.str:
        '''Uniquely identifies a backup plan.

        :cloudformationAttribute: BackupPlanId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBackupPlanId"))

    @builtins.property
    @jsii.member(jsii_name="attrVersionId")
    def attr_version_id(self) -> builtins.str:
        '''Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long.

        Version Ids cannot be edited.

        :cloudformationAttribute: VersionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVersionId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="backupPlan")
    def backup_plan(
        self,
    ) -> typing.Union["CfnBackupPlan.BackupPlanResourceTypeProperty", _aws_cdk_core_f4b25747.IResolvable]:
        '''Uniquely identifies the backup plan to be associated with the selection of resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html#cfn-backup-backupplan-backupplan
        '''
        return typing.cast(typing.Union["CfnBackupPlan.BackupPlanResourceTypeProperty", _aws_cdk_core_f4b25747.IResolvable], jsii.get(self, "backupPlan"))

    @backup_plan.setter
    def backup_plan(
        self,
        value: typing.Union["CfnBackupPlan.BackupPlanResourceTypeProperty", _aws_cdk_core_f4b25747.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dac3f789c2cd24168a7fbf45b8121e0024e194d459e2d5b9774c34764fceedf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupPlan", value)

    @builtins.property
    @jsii.member(jsii_name="backupPlanTags")
    def backup_plan_tags(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        '''To help organize your resources, you can assign your own metadata to the resources that you create.

        Each tag is a key-value pair. The specified tags are assigned to all backups created with this plan.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html#cfn-backup-backupplan-backupplantags
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "backupPlanTags"))

    @backup_plan_tags.setter
    def backup_plan_tags(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b032275b97a5a5e761ea70ab9ff73690e62462e878adf18a5fab7ddf0369feb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupPlanTags", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-backup.CfnBackupPlan.AdvancedBackupSettingResourceTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "backup_options": "backupOptions",
            "resource_type": "resourceType",
        },
    )
    class AdvancedBackupSettingResourceTypeProperty:
        def __init__(
            self,
            *,
            backup_options: typing.Any,
            resource_type: builtins.str,
        ) -> None:
            '''Specifies an object containing resource type and backup options.

            This is only supported for Windows VSS backups.

            :param backup_options: The backup option for the resource. Each option is a key-value pair.
            :param resource_type: The name of a resource type. The only supported resource type is EC2.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-advancedbackupsettingresourcetype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_backup as backup
                
                # backup_options: Any
                
                advanced_backup_setting_resource_type_property = backup.CfnBackupPlan.AdvancedBackupSettingResourceTypeProperty(
                    backup_options=backup_options,
                    resource_type="resourceType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__37f7df21270f46f72d0ffb25481fcf96303c4aec101812a683ecce4365d17acd)
                check_type(argname="argument backup_options", value=backup_options, expected_type=type_hints["backup_options"])
                check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "backup_options": backup_options,
                "resource_type": resource_type,
            }

        @builtins.property
        def backup_options(self) -> typing.Any:
            '''The backup option for the resource.

            Each option is a key-value pair.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-advancedbackupsettingresourcetype.html#cfn-backup-backupplan-advancedbackupsettingresourcetype-backupoptions
            '''
            result = self._values.get("backup_options")
            assert result is not None, "Required property 'backup_options' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def resource_type(self) -> builtins.str:
            '''The name of a resource type.

            The only supported resource type is EC2.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-advancedbackupsettingresourcetype.html#cfn-backup-backupplan-advancedbackupsettingresourcetype-resourcetype
            '''
            result = self._values.get("resource_type")
            assert result is not None, "Required property 'resource_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdvancedBackupSettingResourceTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-backup.CfnBackupPlan.BackupPlanResourceTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "backup_plan_name": "backupPlanName",
            "backup_plan_rule": "backupPlanRule",
            "advanced_backup_settings": "advancedBackupSettings",
        },
    )
    class BackupPlanResourceTypeProperty:
        def __init__(
            self,
            *,
            backup_plan_name: builtins.str,
            backup_plan_rule: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[typing.Union["CfnBackupPlan.BackupRuleResourceTypeProperty", typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]]],
            advanced_backup_settings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnBackupPlan.AdvancedBackupSettingResourceTypeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Specifies an object containing properties used to create a backup plan.

            :param backup_plan_name: The display name of a backup plan.
            :param backup_plan_rule: An array of ``BackupRule`` objects, each of which specifies a scheduled task that is used to back up a selection of resources.
            :param advanced_backup_settings: A list of backup options for each resource type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupplanresourcetype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_backup as backup
                
                # backup_options: Any
                
                backup_plan_resource_type_property = backup.CfnBackupPlan.BackupPlanResourceTypeProperty(
                    backup_plan_name="backupPlanName",
                    backup_plan_rule=[backup.CfnBackupPlan.BackupRuleResourceTypeProperty(
                        rule_name="ruleName",
                        target_backup_vault="targetBackupVault",
                
                        # the properties below are optional
                        completion_window_minutes=123,
                        copy_actions=[backup.CfnBackupPlan.CopyActionResourceTypeProperty(
                            destination_backup_vault_arn="destinationBackupVaultArn",
                
                            # the properties below are optional
                            lifecycle=backup.CfnBackupPlan.LifecycleResourceTypeProperty(
                                delete_after_days=123,
                                move_to_cold_storage_after_days=123
                            )
                        )],
                        enable_continuous_backup=False,
                        lifecycle=backup.CfnBackupPlan.LifecycleResourceTypeProperty(
                            delete_after_days=123,
                            move_to_cold_storage_after_days=123
                        ),
                        recovery_point_tags={
                            "recovery_point_tags_key": "recoveryPointTags"
                        },
                        schedule_expression="scheduleExpression",
                        start_window_minutes=123
                    )],
                
                    # the properties below are optional
                    advanced_backup_settings=[backup.CfnBackupPlan.AdvancedBackupSettingResourceTypeProperty(
                        backup_options=backup_options,
                        resource_type="resourceType"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e5f7cc39f3ac3b75a6c9fd58cfc58413995b84b26a74781a055d8edc4f49d13a)
                check_type(argname="argument backup_plan_name", value=backup_plan_name, expected_type=type_hints["backup_plan_name"])
                check_type(argname="argument backup_plan_rule", value=backup_plan_rule, expected_type=type_hints["backup_plan_rule"])
                check_type(argname="argument advanced_backup_settings", value=advanced_backup_settings, expected_type=type_hints["advanced_backup_settings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "backup_plan_name": backup_plan_name,
                "backup_plan_rule": backup_plan_rule,
            }
            if advanced_backup_settings is not None:
                self._values["advanced_backup_settings"] = advanced_backup_settings

        @builtins.property
        def backup_plan_name(self) -> builtins.str:
            '''The display name of a backup plan.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupplanresourcetype.html#cfn-backup-backupplan-backupplanresourcetype-backupplanname
            '''
            result = self._values.get("backup_plan_name")
            assert result is not None, "Required property 'backup_plan_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def backup_plan_rule(
            self,
        ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union["CfnBackupPlan.BackupRuleResourceTypeProperty", _aws_cdk_core_f4b25747.IResolvable]]]:
            '''An array of ``BackupRule`` objects, each of which specifies a scheduled task that is used to back up a selection of resources.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupplanresourcetype.html#cfn-backup-backupplan-backupplanresourcetype-backupplanrule
            '''
            result = self._values.get("backup_plan_rule")
            assert result is not None, "Required property 'backup_plan_rule' is missing"
            return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union["CfnBackupPlan.BackupRuleResourceTypeProperty", _aws_cdk_core_f4b25747.IResolvable]]], result)

        @builtins.property
        def advanced_backup_settings(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupPlan.AdvancedBackupSettingResourceTypeProperty"]]]]:
            '''A list of backup options for each resource type.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupplanresourcetype.html#cfn-backup-backupplan-backupplanresourcetype-advancedbackupsettings
            '''
            result = self._values.get("advanced_backup_settings")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupPlan.AdvancedBackupSettingResourceTypeProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BackupPlanResourceTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-backup.CfnBackupPlan.BackupRuleResourceTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "rule_name": "ruleName",
            "target_backup_vault": "targetBackupVault",
            "completion_window_minutes": "completionWindowMinutes",
            "copy_actions": "copyActions",
            "enable_continuous_backup": "enableContinuousBackup",
            "lifecycle": "lifecycle",
            "recovery_point_tags": "recoveryPointTags",
            "schedule_expression": "scheduleExpression",
            "start_window_minutes": "startWindowMinutes",
        },
    )
    class BackupRuleResourceTypeProperty:
        def __init__(
            self,
            *,
            rule_name: builtins.str,
            target_backup_vault: builtins.str,
            completion_window_minutes: typing.Optional[jsii.Number] = None,
            copy_actions: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnBackupPlan.CopyActionResourceTypeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            enable_continuous_backup: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            lifecycle: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnBackupPlan.LifecycleResourceTypeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            recovery_point_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
            schedule_expression: typing.Optional[builtins.str] = None,
            start_window_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Specifies an object containing properties used to schedule a task to back up a selection of resources.

            :param rule_name: A display name for a backup rule.
            :param target_backup_vault: The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of letters, numbers, and hyphens.
            :param completion_window_minutes: A value in minutes after a backup job is successfully started before it must be completed or it is canceled by AWS Backup .
            :param copy_actions: An array of CopyAction objects, which contains the details of the copy operation.
            :param enable_continuous_backup: Enables continuous backup and point-in-time restores (PITR).
            :param lifecycle: The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define.
            :param recovery_point_tags: To help organize your resources, you can assign your own metadata to the resources that you create. Each tag is a key-value pair.
            :param schedule_expression: A CRON expression specifying when AWS Backup initiates a backup job.
            :param start_window_minutes: An optional value that specifies a period of time in minutes after a backup is scheduled before a job is canceled if it doesn't start successfully. If this value is included, it must be at least 60 minutes to avoid errors.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_backup as backup
                
                backup_rule_resource_type_property = backup.CfnBackupPlan.BackupRuleResourceTypeProperty(
                    rule_name="ruleName",
                    target_backup_vault="targetBackupVault",
                
                    # the properties below are optional
                    completion_window_minutes=123,
                    copy_actions=[backup.CfnBackupPlan.CopyActionResourceTypeProperty(
                        destination_backup_vault_arn="destinationBackupVaultArn",
                
                        # the properties below are optional
                        lifecycle=backup.CfnBackupPlan.LifecycleResourceTypeProperty(
                            delete_after_days=123,
                            move_to_cold_storage_after_days=123
                        )
                    )],
                    enable_continuous_backup=False,
                    lifecycle=backup.CfnBackupPlan.LifecycleResourceTypeProperty(
                        delete_after_days=123,
                        move_to_cold_storage_after_days=123
                    ),
                    recovery_point_tags={
                        "recovery_point_tags_key": "recoveryPointTags"
                    },
                    schedule_expression="scheduleExpression",
                    start_window_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b287ba37827873fa303fa78a2cb621bcccc06adad7b5caa70bb3dceb6166e106)
                check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
                check_type(argname="argument target_backup_vault", value=target_backup_vault, expected_type=type_hints["target_backup_vault"])
                check_type(argname="argument completion_window_minutes", value=completion_window_minutes, expected_type=type_hints["completion_window_minutes"])
                check_type(argname="argument copy_actions", value=copy_actions, expected_type=type_hints["copy_actions"])
                check_type(argname="argument enable_continuous_backup", value=enable_continuous_backup, expected_type=type_hints["enable_continuous_backup"])
                check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
                check_type(argname="argument recovery_point_tags", value=recovery_point_tags, expected_type=type_hints["recovery_point_tags"])
                check_type(argname="argument schedule_expression", value=schedule_expression, expected_type=type_hints["schedule_expression"])
                check_type(argname="argument start_window_minutes", value=start_window_minutes, expected_type=type_hints["start_window_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "rule_name": rule_name,
                "target_backup_vault": target_backup_vault,
            }
            if completion_window_minutes is not None:
                self._values["completion_window_minutes"] = completion_window_minutes
            if copy_actions is not None:
                self._values["copy_actions"] = copy_actions
            if enable_continuous_backup is not None:
                self._values["enable_continuous_backup"] = enable_continuous_backup
            if lifecycle is not None:
                self._values["lifecycle"] = lifecycle
            if recovery_point_tags is not None:
                self._values["recovery_point_tags"] = recovery_point_tags
            if schedule_expression is not None:
                self._values["schedule_expression"] = schedule_expression
            if start_window_minutes is not None:
                self._values["start_window_minutes"] = start_window_minutes

        @builtins.property
        def rule_name(self) -> builtins.str:
            '''A display name for a backup rule.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-rulename
            '''
            result = self._values.get("rule_name")
            assert result is not None, "Required property 'rule_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target_backup_vault(self) -> builtins.str:
            '''The name of a logical container where backups are stored.

            Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of letters, numbers, and hyphens.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-targetbackupvault
            '''
            result = self._values.get("target_backup_vault")
            assert result is not None, "Required property 'target_backup_vault' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def completion_window_minutes(self) -> typing.Optional[jsii.Number]:
            '''A value in minutes after a backup job is successfully started before it must be completed or it is canceled by AWS Backup .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-completionwindowminutes
            '''
            result = self._values.get("completion_window_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def copy_actions(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupPlan.CopyActionResourceTypeProperty"]]]]:
            '''An array of CopyAction objects, which contains the details of the copy operation.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-copyactions
            '''
            result = self._values.get("copy_actions")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupPlan.CopyActionResourceTypeProperty"]]]], result)

        @builtins.property
        def enable_continuous_backup(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''Enables continuous backup and point-in-time restores (PITR).

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-enablecontinuousbackup
            '''
            result = self._values.get("enable_continuous_backup")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def lifecycle(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupPlan.LifecycleResourceTypeProperty"]]:
            '''The lifecycle defines when a protected resource is transitioned to cold storage and when it expires.

            AWS Backup transitions and expires backups automatically according to the lifecycle that you define.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-lifecycle
            '''
            result = self._values.get("lifecycle")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupPlan.LifecycleResourceTypeProperty"]], result)

        @builtins.property
        def recovery_point_tags(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''To help organize your resources, you can assign your own metadata to the resources that you create.

            Each tag is a key-value pair.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-recoverypointtags
            '''
            result = self._values.get("recovery_point_tags")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def schedule_expression(self) -> typing.Optional[builtins.str]:
            '''A CRON expression specifying when AWS Backup initiates a backup job.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-scheduleexpression
            '''
            result = self._values.get("schedule_expression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def start_window_minutes(self) -> typing.Optional[jsii.Number]:
            '''An optional value that specifies a period of time in minutes after a backup is scheduled before a job is canceled if it doesn't start successfully.

            If this value is included, it must be at least 60 minutes to avoid errors.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-backupruleresourcetype.html#cfn-backup-backupplan-backupruleresourcetype-startwindowminutes
            '''
            result = self._values.get("start_window_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BackupRuleResourceTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-backup.CfnBackupPlan.CopyActionResourceTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_backup_vault_arn": "destinationBackupVaultArn",
            "lifecycle": "lifecycle",
        },
    )
    class CopyActionResourceTypeProperty:
        def __init__(
            self,
            *,
            destination_backup_vault_arn: builtins.str,
            lifecycle: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnBackupPlan.LifecycleResourceTypeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Copies backups created by a backup rule to another vault.

            :param destination_backup_vault_arn: An Amazon Resource Name (ARN) that uniquely identifies the destination backup vault for the copied backup. For example, ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault.``
            :param lifecycle: Defines when a protected resource is transitioned to cold storage and when it expires. AWS Backup transitions and expires backups automatically according to the lifecycle that you define. If you do not specify a lifecycle, AWS Backup applies the lifecycle policy of the source backup to the destination backup. Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-copyactionresourcetype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_backup as backup
                
                copy_action_resource_type_property = backup.CfnBackupPlan.CopyActionResourceTypeProperty(
                    destination_backup_vault_arn="destinationBackupVaultArn",
                
                    # the properties below are optional
                    lifecycle=backup.CfnBackupPlan.LifecycleResourceTypeProperty(
                        delete_after_days=123,
                        move_to_cold_storage_after_days=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9c8d9238e6c9aad30f4707d2a0bb5dfb22ffa1f941fbb53b8ffcaf42896f3f27)
                check_type(argname="argument destination_backup_vault_arn", value=destination_backup_vault_arn, expected_type=type_hints["destination_backup_vault_arn"])
                check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination_backup_vault_arn": destination_backup_vault_arn,
            }
            if lifecycle is not None:
                self._values["lifecycle"] = lifecycle

        @builtins.property
        def destination_backup_vault_arn(self) -> builtins.str:
            '''An Amazon Resource Name (ARN) that uniquely identifies the destination backup vault for the copied backup.

            For example, ``arn:aws:backup:us-east-1:123456789012:vault:aBackupVault.``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-copyactionresourcetype.html#cfn-backup-backupplan-copyactionresourcetype-destinationbackupvaultarn
            '''
            result = self._values.get("destination_backup_vault_arn")
            assert result is not None, "Required property 'destination_backup_vault_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def lifecycle(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupPlan.LifecycleResourceTypeProperty"]]:
            '''Defines when a protected resource is transitioned to cold storage and when it expires.

            AWS Backup transitions and expires backups automatically according to the lifecycle that you define. If you do not specify a lifecycle, AWS Backup applies the lifecycle policy of the source backup to the destination backup.

            Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-copyactionresourcetype.html#cfn-backup-backupplan-copyactionresourcetype-lifecycle
            '''
            result = self._values.get("lifecycle")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupPlan.LifecycleResourceTypeProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CopyActionResourceTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-backup.CfnBackupPlan.LifecycleResourceTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delete_after_days": "deleteAfterDays",
            "move_to_cold_storage_after_days": "moveToColdStorageAfterDays",
        },
    )
    class LifecycleResourceTypeProperty:
        def __init__(
            self,
            *,
            delete_after_days: typing.Optional[jsii.Number] = None,
            move_to_cold_storage_after_days: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Specifies an object containing an array of ``Transition`` objects that determine how long in days before a recovery point transitions to cold storage or is deleted.

            :param delete_after_days: Specifies the number of days after creation that a recovery point is deleted. Must be greater than ``MoveToColdStorageAfterDays`` .
            :param move_to_cold_storage_after_days: Specifies the number of days after creation that a recovery point is moved to cold storage.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-lifecycleresourcetype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_backup as backup
                
                lifecycle_resource_type_property = backup.CfnBackupPlan.LifecycleResourceTypeProperty(
                    delete_after_days=123,
                    move_to_cold_storage_after_days=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f95ac72cdea9b5f2d90003a177be25c89cc7cc2e9a5afc0bdd407cd6a15cbf99)
                check_type(argname="argument delete_after_days", value=delete_after_days, expected_type=type_hints["delete_after_days"])
                check_type(argname="argument move_to_cold_storage_after_days", value=move_to_cold_storage_after_days, expected_type=type_hints["move_to_cold_storage_after_days"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if delete_after_days is not None:
                self._values["delete_after_days"] = delete_after_days
            if move_to_cold_storage_after_days is not None:
                self._values["move_to_cold_storage_after_days"] = move_to_cold_storage_after_days

        @builtins.property
        def delete_after_days(self) -> typing.Optional[jsii.Number]:
            '''Specifies the number of days after creation that a recovery point is deleted.

            Must be greater than ``MoveToColdStorageAfterDays`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-lifecycleresourcetype.html#cfn-backup-backupplan-lifecycleresourcetype-deleteafterdays
            '''
            result = self._values.get("delete_after_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def move_to_cold_storage_after_days(self) -> typing.Optional[jsii.Number]:
            '''Specifies the number of days after creation that a recovery point is moved to cold storage.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupplan-lifecycleresourcetype.html#cfn-backup-backupplan-lifecycleresourcetype-movetocoldstorageafterdays
            '''
            result = self._values.get("move_to_cold_storage_after_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LifecycleResourceTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-backup.CfnBackupPlanProps",
    jsii_struct_bases=[],
    name_mapping={"backup_plan": "backupPlan", "backup_plan_tags": "backupPlanTags"},
)
class CfnBackupPlanProps:
    def __init__(
        self,
        *,
        backup_plan: typing.Union[typing.Union[CfnBackupPlan.BackupPlanResourceTypeProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable],
        backup_plan_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnBackupPlan``.

        :param backup_plan: Uniquely identifies the backup plan to be associated with the selection of resources.
        :param backup_plan_tags: To help organize your resources, you can assign your own metadata to the resources that you create. Each tag is a key-value pair. The specified tags are assigned to all backups created with this plan.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_backup as backup
            
            # backup_options: Any
            
            cfn_backup_plan_props = backup.CfnBackupPlanProps(
                backup_plan=backup.CfnBackupPlan.BackupPlanResourceTypeProperty(
                    backup_plan_name="backupPlanName",
                    backup_plan_rule=[backup.CfnBackupPlan.BackupRuleResourceTypeProperty(
                        rule_name="ruleName",
                        target_backup_vault="targetBackupVault",
            
                        # the properties below are optional
                        completion_window_minutes=123,
                        copy_actions=[backup.CfnBackupPlan.CopyActionResourceTypeProperty(
                            destination_backup_vault_arn="destinationBackupVaultArn",
            
                            # the properties below are optional
                            lifecycle=backup.CfnBackupPlan.LifecycleResourceTypeProperty(
                                delete_after_days=123,
                                move_to_cold_storage_after_days=123
                            )
                        )],
                        enable_continuous_backup=False,
                        lifecycle=backup.CfnBackupPlan.LifecycleResourceTypeProperty(
                            delete_after_days=123,
                            move_to_cold_storage_after_days=123
                        ),
                        recovery_point_tags={
                            "recovery_point_tags_key": "recoveryPointTags"
                        },
                        schedule_expression="scheduleExpression",
                        start_window_minutes=123
                    )],
            
                    # the properties below are optional
                    advanced_backup_settings=[backup.CfnBackupPlan.AdvancedBackupSettingResourceTypeProperty(
                        backup_options=backup_options,
                        resource_type="resourceType"
                    )]
                ),
            
                # the properties below are optional
                backup_plan_tags={
                    "backup_plan_tags_key": "backupPlanTags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78bebf496bb7fbd732b6e916ccfc48ca7f82bb04b0fc30275559a53a691d2769)
            check_type(argname="argument backup_plan", value=backup_plan, expected_type=type_hints["backup_plan"])
            check_type(argname="argument backup_plan_tags", value=backup_plan_tags, expected_type=type_hints["backup_plan_tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "backup_plan": backup_plan,
        }
        if backup_plan_tags is not None:
            self._values["backup_plan_tags"] = backup_plan_tags

    @builtins.property
    def backup_plan(
        self,
    ) -> typing.Union[CfnBackupPlan.BackupPlanResourceTypeProperty, _aws_cdk_core_f4b25747.IResolvable]:
        '''Uniquely identifies the backup plan to be associated with the selection of resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html#cfn-backup-backupplan-backupplan
        '''
        result = self._values.get("backup_plan")
        assert result is not None, "Required property 'backup_plan' is missing"
        return typing.cast(typing.Union[CfnBackupPlan.BackupPlanResourceTypeProperty, _aws_cdk_core_f4b25747.IResolvable], result)

    @builtins.property
    def backup_plan_tags(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        '''To help organize your resources, you can assign your own metadata to the resources that you create.

        Each tag is a key-value pair. The specified tags are assigned to all backups created with this plan.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html#cfn-backup-backupplan-backupplantags
        '''
        result = self._values.get("backup_plan_tags")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBackupPlanProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnBackupSelection(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-backup.CfnBackupSelection",
):
    '''A CloudFormation ``AWS::Backup::BackupSelection``.

    Specifies a set of resources to assign to a backup plan.

    For a sample AWS CloudFormation template, see the `AWS Backup Developer Guide <https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html#assigning-resources-cfn>`_ .

    :cloudformationResource: AWS::Backup::BackupSelection
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupselection.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_backup as backup
        
        # conditions: Any
        
        cfn_backup_selection = backup.CfnBackupSelection(self, "MyCfnBackupSelection",
            backup_plan_id="backupPlanId",
            backup_selection=backup.CfnBackupSelection.BackupSelectionResourceTypeProperty(
                iam_role_arn="iamRoleArn",
                selection_name="selectionName",
        
                # the properties below are optional
                conditions=conditions,
                list_of_tags=[backup.CfnBackupSelection.ConditionResourceTypeProperty(
                    condition_key="conditionKey",
                    condition_type="conditionType",
                    condition_value="conditionValue"
                )],
                not_resources=["notResources"],
                resources=["resources"]
            )
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        backup_plan_id: builtins.str,
        backup_selection: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnBackupSelection.BackupSelectionResourceTypeProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Create a new ``AWS::Backup::BackupSelection``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param backup_plan_id: Uniquely identifies a backup plan.
        :param backup_selection: Specifies the body of a request to assign a set of resources to a backup plan. It includes an array of resources, an optional array of patterns to exclude resources, an optional role to provide access to the AWS service the resource belongs to, and an optional array of tags used to identify a set of resources.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e45952eebe3d558f21ca31af5c94fba3340cb712051449ea00c8ecebd2690a11)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBackupSelectionProps(
            backup_plan_id=backup_plan_id, backup_selection=backup_selection
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bc2b1b4f654afa86e6ab48546b87357ad30a0b35aa88c97fa84f932cc03783e)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__096ef63dbdd8e69e98ad67a1acc65b7d9a2a5eb1811e7d915bfe826d2a7283e3)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrBackupPlanId")
    def attr_backup_plan_id(self) -> builtins.str:
        '''Uniquely identifies a backup plan.

        :cloudformationAttribute: BackupPlanId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBackupPlanId"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Uniquely identifies the backup selection.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrSelectionId")
    def attr_selection_id(self) -> builtins.str:
        '''Uniquely identifies a request to assign a set of resources to a backup plan.

        :cloudformationAttribute: SelectionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSelectionId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="backupPlanId")
    def backup_plan_id(self) -> builtins.str:
        '''Uniquely identifies a backup plan.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupselection.html#cfn-backup-backupselection-backupplanid
        '''
        return typing.cast(builtins.str, jsii.get(self, "backupPlanId"))

    @backup_plan_id.setter
    def backup_plan_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2470d1708af93b8366f2aab218f52ba5c3bcf56d840f7d8bb710510b9aa4fb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupPlanId", value)

    @builtins.property
    @jsii.member(jsii_name="backupSelection")
    def backup_selection(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupSelection.BackupSelectionResourceTypeProperty"]:
        '''Specifies the body of a request to assign a set of resources to a backup plan.

        It includes an array of resources, an optional array of patterns to exclude resources, an optional role to provide access to the AWS service the resource belongs to, and an optional array of tags used to identify a set of resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupselection.html#cfn-backup-backupselection-backupselection
        '''
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupSelection.BackupSelectionResourceTypeProperty"], jsii.get(self, "backupSelection"))

    @backup_selection.setter
    def backup_selection(
        self,
        value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupSelection.BackupSelectionResourceTypeProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79263fc95edbfd1311eb36845cdf5b605e282bab33688784c01d97c115e64ad4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupSelection", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-backup.CfnBackupSelection.BackupSelectionResourceTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "iam_role_arn": "iamRoleArn",
            "selection_name": "selectionName",
            "conditions": "conditions",
            "list_of_tags": "listOfTags",
            "not_resources": "notResources",
            "resources": "resources",
        },
    )
    class BackupSelectionResourceTypeProperty:
        def __init__(
            self,
            *,
            iam_role_arn: builtins.str,
            selection_name: builtins.str,
            conditions: typing.Any = None,
            list_of_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnBackupSelection.ConditionResourceTypeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            not_resources: typing.Optional[typing.Sequence[builtins.str]] = None,
            resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Specifies an object containing properties used to assign a set of resources to a backup plan.

            :param iam_role_arn: The ARN of the IAM role that AWS Backup uses to authenticate when backing up the target resource; for example, ``arn:aws:iam::123456789012:role/S3Access`` .
            :param selection_name: The display name of a resource selection document.
            :param conditions: A list of conditions that you define to assign resources to your backup plans using tags. For example, ``"StringEquals": { "ConditionKey": "aws:ResourceTag/CreatedByCryo", "ConditionValue": "true" },`` . Condition operators are case sensitive. ``Conditions`` differs from ``ListOfTags`` as follows: - When you specify more than one condition, you only assign the resources that match ALL conditions (using AND logic). - ``Conditions`` supports ``StringEquals`` , ``StringLike`` , ``StringNotEquals`` , and ``StringNotLike`` . ``ListOfTags`` only supports ``StringEquals`` .
            :param list_of_tags: A list of conditions that you define to assign resources to your backup plans using tags. For example, ``"StringEquals": { "ConditionKey": "aws:ResourceTag/CreatedByCryo", "ConditionValue": "true" },`` . Condition operators are case sensitive. ``ListOfTags`` differs from ``Conditions`` as follows: - When you specify more than one condition, you assign all resources that match AT LEAST ONE condition (using OR logic). - ``ListOfTags`` only supports ``StringEquals`` . ``Conditions`` supports ``StringEquals`` , ``StringLike`` , ``StringNotEquals`` , and ``StringNotLike`` .
            :param not_resources: A list of Amazon Resource Names (ARNs) to exclude from a backup plan. The maximum number of ARNs is 500 without wildcards, or 30 ARNs with wildcards. If you need to exclude many resources from a backup plan, consider a different resource selection strategy, such as assigning only one or a few resource types or refining your resource selection using tags.
            :param resources: An array of strings that contain Amazon Resource Names (ARNs) of resources to assign to a backup plan.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_backup as backup
                
                # conditions: Any
                
                backup_selection_resource_type_property = backup.CfnBackupSelection.BackupSelectionResourceTypeProperty(
                    iam_role_arn="iamRoleArn",
                    selection_name="selectionName",
                
                    # the properties below are optional
                    conditions=conditions,
                    list_of_tags=[backup.CfnBackupSelection.ConditionResourceTypeProperty(
                        condition_key="conditionKey",
                        condition_type="conditionType",
                        condition_value="conditionValue"
                    )],
                    not_resources=["notResources"],
                    resources=["resources"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7d62b37b6875ddb2c3923b17f42428c53878f71189ebf25d62ad6bd13c671b0d)
                check_type(argname="argument iam_role_arn", value=iam_role_arn, expected_type=type_hints["iam_role_arn"])
                check_type(argname="argument selection_name", value=selection_name, expected_type=type_hints["selection_name"])
                check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
                check_type(argname="argument list_of_tags", value=list_of_tags, expected_type=type_hints["list_of_tags"])
                check_type(argname="argument not_resources", value=not_resources, expected_type=type_hints["not_resources"])
                check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "iam_role_arn": iam_role_arn,
                "selection_name": selection_name,
            }
            if conditions is not None:
                self._values["conditions"] = conditions
            if list_of_tags is not None:
                self._values["list_of_tags"] = list_of_tags
            if not_resources is not None:
                self._values["not_resources"] = not_resources
            if resources is not None:
                self._values["resources"] = resources

        @builtins.property
        def iam_role_arn(self) -> builtins.str:
            '''The ARN of the IAM role that AWS Backup uses to authenticate when backing up the target resource;

            for example, ``arn:aws:iam::123456789012:role/S3Access`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-iamrolearn
            '''
            result = self._values.get("iam_role_arn")
            assert result is not None, "Required property 'iam_role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def selection_name(self) -> builtins.str:
            '''The display name of a resource selection document.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-selectionname
            '''
            result = self._values.get("selection_name")
            assert result is not None, "Required property 'selection_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def conditions(self) -> typing.Any:
            '''A list of conditions that you define to assign resources to your backup plans using tags.

            For example, ``"StringEquals": { "ConditionKey": "aws:ResourceTag/CreatedByCryo", "ConditionValue": "true" },`` . Condition operators are case sensitive.

            ``Conditions`` differs from ``ListOfTags`` as follows:

            - When you specify more than one condition, you only assign the resources that match ALL conditions (using AND logic).
            - ``Conditions`` supports ``StringEquals`` , ``StringLike`` , ``StringNotEquals`` , and ``StringNotLike`` . ``ListOfTags`` only supports ``StringEquals`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-conditions
            '''
            result = self._values.get("conditions")
            return typing.cast(typing.Any, result)

        @builtins.property
        def list_of_tags(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupSelection.ConditionResourceTypeProperty"]]]]:
            '''A list of conditions that you define to assign resources to your backup plans using tags.

            For example, ``"StringEquals": { "ConditionKey": "aws:ResourceTag/CreatedByCryo", "ConditionValue": "true" },`` . Condition operators are case sensitive.

            ``ListOfTags`` differs from ``Conditions`` as follows:

            - When you specify more than one condition, you assign all resources that match AT LEAST ONE condition (using OR logic).
            - ``ListOfTags`` only supports ``StringEquals`` . ``Conditions`` supports ``StringEquals`` , ``StringLike`` , ``StringNotEquals`` , and ``StringNotLike`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-listoftags
            '''
            result = self._values.get("list_of_tags")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupSelection.ConditionResourceTypeProperty"]]]], result)

        @builtins.property
        def not_resources(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of Amazon Resource Names (ARNs) to exclude from a backup plan.

            The maximum number of ARNs is 500 without wildcards, or 30 ARNs with wildcards.

            If you need to exclude many resources from a backup plan, consider a different resource selection strategy, such as assigning only one or a few resource types or refining your resource selection using tags.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-notresources
            '''
            result = self._values.get("not_resources")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def resources(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An array of strings that contain Amazon Resource Names (ARNs) of resources to assign to a backup plan.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-backupselectionresourcetype.html#cfn-backup-backupselection-backupselectionresourcetype-resources
            '''
            result = self._values.get("resources")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BackupSelectionResourceTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-backup.CfnBackupSelection.ConditionParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "condition_key": "conditionKey",
            "condition_value": "conditionValue",
        },
    )
    class ConditionParameterProperty:
        def __init__(
            self,
            *,
            condition_key: typing.Optional[builtins.str] = None,
            condition_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Includes information about tags you define to assign tagged resources to a backup plan.

            :param condition_key: The key in a key-value pair. For example, in the tag ``Department: Accounting`` , ``Department`` is the key.
            :param condition_value: The value in a key-value pair. For example, in the tag ``Department: Accounting`` , ``Accounting`` is the value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_backup as backup
                
                condition_parameter_property = backup.CfnBackupSelection.ConditionParameterProperty(
                    condition_key="conditionKey",
                    condition_value="conditionValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2ec2e118c097ddebac2dc76684f7ba1089b042c2c95d9df88739a851ed302d1b)
                check_type(argname="argument condition_key", value=condition_key, expected_type=type_hints["condition_key"])
                check_type(argname="argument condition_value", value=condition_value, expected_type=type_hints["condition_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if condition_key is not None:
                self._values["condition_key"] = condition_key
            if condition_value is not None:
                self._values["condition_value"] = condition_value

        @builtins.property
        def condition_key(self) -> typing.Optional[builtins.str]:
            '''The key in a key-value pair.

            For example, in the tag ``Department: Accounting`` , ``Department`` is the key.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionparameter.html#cfn-backup-backupselection-conditionparameter-conditionkey
            '''
            result = self._values.get("condition_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def condition_value(self) -> typing.Optional[builtins.str]:
            '''The value in a key-value pair.

            For example, in the tag ``Department: Accounting`` , ``Accounting`` is the value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionparameter.html#cfn-backup-backupselection-conditionparameter-conditionvalue
            '''
            result = self._values.get("condition_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConditionParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-backup.CfnBackupSelection.ConditionResourceTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "condition_key": "conditionKey",
            "condition_type": "conditionType",
            "condition_value": "conditionValue",
        },
    )
    class ConditionResourceTypeProperty:
        def __init__(
            self,
            *,
            condition_key: builtins.str,
            condition_type: builtins.str,
            condition_value: builtins.str,
        ) -> None:
            '''Specifies an object that contains an array of triplets made up of a condition type (such as ``STRINGEQUALS`` ), a key, and a value.

            Conditions are used to filter resources in a selection that is assigned to a backup plan.

            :param condition_key: The key in a key-value pair. For example, in ``"Department": "accounting"`` , ``"Department"`` is the key.
            :param condition_type: An operation, such as ``STRINGEQUALS`` , that is applied to a key-value pair used to filter resources in a selection.
            :param condition_value: The value in a key-value pair. For example, in ``"Department": "accounting"`` , ``"accounting"`` is the value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionresourcetype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_backup as backup
                
                condition_resource_type_property = backup.CfnBackupSelection.ConditionResourceTypeProperty(
                    condition_key="conditionKey",
                    condition_type="conditionType",
                    condition_value="conditionValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__230351d0c592b9ae2495166fc873edea23b9c56fcd59196f005253a3797b8a78)
                check_type(argname="argument condition_key", value=condition_key, expected_type=type_hints["condition_key"])
                check_type(argname="argument condition_type", value=condition_type, expected_type=type_hints["condition_type"])
                check_type(argname="argument condition_value", value=condition_value, expected_type=type_hints["condition_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "condition_key": condition_key,
                "condition_type": condition_type,
                "condition_value": condition_value,
            }

        @builtins.property
        def condition_key(self) -> builtins.str:
            '''The key in a key-value pair.

            For example, in ``"Department": "accounting"`` , ``"Department"`` is the key.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionresourcetype.html#cfn-backup-backupselection-conditionresourcetype-conditionkey
            '''
            result = self._values.get("condition_key")
            assert result is not None, "Required property 'condition_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def condition_type(self) -> builtins.str:
            '''An operation, such as ``STRINGEQUALS`` , that is applied to a key-value pair used to filter resources in a selection.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionresourcetype.html#cfn-backup-backupselection-conditionresourcetype-conditiontype
            '''
            result = self._values.get("condition_type")
            assert result is not None, "Required property 'condition_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def condition_value(self) -> builtins.str:
            '''The value in a key-value pair.

            For example, in ``"Department": "accounting"`` , ``"accounting"`` is the value.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditionresourcetype.html#cfn-backup-backupselection-conditionresourcetype-conditionvalue
            '''
            result = self._values.get("condition_value")
            assert result is not None, "Required property 'condition_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConditionResourceTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-backup.CfnBackupSelection.ConditionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "string_equals": "stringEquals",
            "string_like": "stringLike",
            "string_not_equals": "stringNotEquals",
            "string_not_like": "stringNotLike",
        },
    )
    class ConditionsProperty:
        def __init__(
            self,
            *,
            string_equals: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnBackupSelection.ConditionParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            string_like: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnBackupSelection.ConditionParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            string_not_equals: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnBackupSelection.ConditionParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            string_not_like: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnBackupSelection.ConditionParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Contains information about which resources to include or exclude from a backup plan using their tags.

            Conditions are case sensitive.

            :param string_equals: Filters the values of your tagged resources for only those resources that you tagged with the same value. Also called "exact matching."
            :param string_like: Filters the values of your tagged resources for matching tag values with the use of a wildcard character (*) anywhere in the string. For example, "prod*" or "*rod*" matches the tag value "production".
            :param string_not_equals: Filters the values of your tagged resources for only those resources that you tagged that do not have the same value. Also called "negated matching."
            :param string_not_like: Filters the values of your tagged resources for non-matching tag values with the use of a wildcard character (*) anywhere in the string.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_backup as backup
                
                conditions_property = backup.CfnBackupSelection.ConditionsProperty(
                    string_equals=[backup.CfnBackupSelection.ConditionParameterProperty(
                        condition_key="conditionKey",
                        condition_value="conditionValue"
                    )],
                    string_like=[backup.CfnBackupSelection.ConditionParameterProperty(
                        condition_key="conditionKey",
                        condition_value="conditionValue"
                    )],
                    string_not_equals=[backup.CfnBackupSelection.ConditionParameterProperty(
                        condition_key="conditionKey",
                        condition_value="conditionValue"
                    )],
                    string_not_like=[backup.CfnBackupSelection.ConditionParameterProperty(
                        condition_key="conditionKey",
                        condition_value="conditionValue"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__11ea9a50ad5cd9c04f7c48fcd3af05da80d6c0c32872d98a35450fe492127617)
                check_type(argname="argument string_equals", value=string_equals, expected_type=type_hints["string_equals"])
                check_type(argname="argument string_like", value=string_like, expected_type=type_hints["string_like"])
                check_type(argname="argument string_not_equals", value=string_not_equals, expected_type=type_hints["string_not_equals"])
                check_type(argname="argument string_not_like", value=string_not_like, expected_type=type_hints["string_not_like"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if string_equals is not None:
                self._values["string_equals"] = string_equals
            if string_like is not None:
                self._values["string_like"] = string_like
            if string_not_equals is not None:
                self._values["string_not_equals"] = string_not_equals
            if string_not_like is not None:
                self._values["string_not_like"] = string_not_like

        @builtins.property
        def string_equals(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupSelection.ConditionParameterProperty"]]]]:
            '''Filters the values of your tagged resources for only those resources that you tagged with the same value.

            Also called "exact matching."

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditions.html#cfn-backup-backupselection-conditions-stringequals
            '''
            result = self._values.get("string_equals")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupSelection.ConditionParameterProperty"]]]], result)

        @builtins.property
        def string_like(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupSelection.ConditionParameterProperty"]]]]:
            '''Filters the values of your tagged resources for matching tag values with the use of a wildcard character (*) anywhere in the string.

            For example, "prod*" or "*rod*" matches the tag value "production".

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditions.html#cfn-backup-backupselection-conditions-stringlike
            '''
            result = self._values.get("string_like")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupSelection.ConditionParameterProperty"]]]], result)

        @builtins.property
        def string_not_equals(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupSelection.ConditionParameterProperty"]]]]:
            '''Filters the values of your tagged resources for only those resources that you tagged that do not have the same value.

            Also called "negated matching."

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditions.html#cfn-backup-backupselection-conditions-stringnotequals
            '''
            result = self._values.get("string_not_equals")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupSelection.ConditionParameterProperty"]]]], result)

        @builtins.property
        def string_not_like(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupSelection.ConditionParameterProperty"]]]]:
            '''Filters the values of your tagged resources for non-matching tag values with the use of a wildcard character (*) anywhere in the string.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupselection-conditions.html#cfn-backup-backupselection-conditions-stringnotlike
            '''
            result = self._values.get("string_not_like")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupSelection.ConditionParameterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConditionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-backup.CfnBackupSelectionProps",
    jsii_struct_bases=[],
    name_mapping={
        "backup_plan_id": "backupPlanId",
        "backup_selection": "backupSelection",
    },
)
class CfnBackupSelectionProps:
    def __init__(
        self,
        *,
        backup_plan_id: builtins.str,
        backup_selection: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnBackupSelection.BackupSelectionResourceTypeProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnBackupSelection``.

        :param backup_plan_id: Uniquely identifies a backup plan.
        :param backup_selection: Specifies the body of a request to assign a set of resources to a backup plan. It includes an array of resources, an optional array of patterns to exclude resources, an optional role to provide access to the AWS service the resource belongs to, and an optional array of tags used to identify a set of resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupselection.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_backup as backup
            
            # conditions: Any
            
            cfn_backup_selection_props = backup.CfnBackupSelectionProps(
                backup_plan_id="backupPlanId",
                backup_selection=backup.CfnBackupSelection.BackupSelectionResourceTypeProperty(
                    iam_role_arn="iamRoleArn",
                    selection_name="selectionName",
            
                    # the properties below are optional
                    conditions=conditions,
                    list_of_tags=[backup.CfnBackupSelection.ConditionResourceTypeProperty(
                        condition_key="conditionKey",
                        condition_type="conditionType",
                        condition_value="conditionValue"
                    )],
                    not_resources=["notResources"],
                    resources=["resources"]
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a930a5cebaac7ba7f173bb848cfc290d9d01bd4205bf5f3650ceb467d3d7a07)
            check_type(argname="argument backup_plan_id", value=backup_plan_id, expected_type=type_hints["backup_plan_id"])
            check_type(argname="argument backup_selection", value=backup_selection, expected_type=type_hints["backup_selection"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "backup_plan_id": backup_plan_id,
            "backup_selection": backup_selection,
        }

    @builtins.property
    def backup_plan_id(self) -> builtins.str:
        '''Uniquely identifies a backup plan.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupselection.html#cfn-backup-backupselection-backupplanid
        '''
        result = self._values.get("backup_plan_id")
        assert result is not None, "Required property 'backup_plan_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def backup_selection(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnBackupSelection.BackupSelectionResourceTypeProperty]:
        '''Specifies the body of a request to assign a set of resources to a backup plan.

        It includes an array of resources, an optional array of patterns to exclude resources, an optional role to provide access to the AWS service the resource belongs to, and an optional array of tags used to identify a set of resources.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupselection.html#cfn-backup-backupselection-backupselection
        '''
        result = self._values.get("backup_selection")
        assert result is not None, "Required property 'backup_selection' is missing"
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnBackupSelection.BackupSelectionResourceTypeProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBackupSelectionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnBackupVault(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-backup.CfnBackupVault",
):
    '''A CloudFormation ``AWS::Backup::BackupVault``.

    Creates a logical container where backups are stored. A ``CreateBackupVault`` request includes a name, optionally one or more resource tags, an encryption key, and a request ID.

    Do not include sensitive data, such as passport numbers, in the name of a backup vault.

    For a sample AWS CloudFormation template, see the `AWS Backup Developer Guide <https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html#assigning-resources-cfn>`_ .

    :cloudformationResource: AWS::Backup::BackupVault
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_backup as backup
        
        # access_policy: Any
        
        cfn_backup_vault = backup.CfnBackupVault(self, "MyCfnBackupVault",
            backup_vault_name="backupVaultName",
        
            # the properties below are optional
            access_policy=access_policy,
            backup_vault_tags={
                "backup_vault_tags_key": "backupVaultTags"
            },
            encryption_key_arn="encryptionKeyArn",
            lock_configuration=backup.CfnBackupVault.LockConfigurationTypeProperty(
                min_retention_days=123,
        
                # the properties below are optional
                changeable_for_days=123,
                max_retention_days=123
            ),
            notifications=backup.CfnBackupVault.NotificationObjectTypeProperty(
                backup_vault_events=["backupVaultEvents"],
                sns_topic_arn="snsTopicArn"
            )
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        backup_vault_name: builtins.str,
        access_policy: typing.Any = None,
        backup_vault_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        encryption_key_arn: typing.Optional[builtins.str] = None,
        lock_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnBackupVault.LockConfigurationTypeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        notifications: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnBackupVault.NotificationObjectTypeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Backup::BackupVault``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param backup_vault_name: The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
        :param access_policy: A resource-based policy that is used to manage access permissions on the target backup vault.
        :param backup_vault_tags: Metadata that you can assign to help organize the resources that you create. Each tag is a key-value pair.
        :param encryption_key_arn: A server-side encryption key you can specify to encrypt your backups from services that support full AWS Backup management; for example, ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` . If you specify a key, you must specify its ARN, not its alias. If you do not specify a key, AWS Backup creates a KMS key for you by default. To learn which AWS Backup services support full AWS Backup management and how AWS Backup handles encryption for backups from services that do not yet support full AWS Backup , see `Encryption for backups in AWS Backup <https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html>`_
        :param lock_configuration: Configuration for `AWS Backup Vault Lock <https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html>`_ .
        :param notifications: The SNS event notifications for the specified backup vault.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7d0abd4b6c6f24669a1eaaab8bdefecbe7b5f458c5bfd19fc926cf6bed2adb5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBackupVaultProps(
            backup_vault_name=backup_vault_name,
            access_policy=access_policy,
            backup_vault_tags=backup_vault_tags,
            encryption_key_arn=encryption_key_arn,
            lock_configuration=lock_configuration,
            notifications=notifications,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19a3d21b3f993f6310da73cd1b52794a2cf4ab173c1c1a7c10af4c986235fe67)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86fe929c5f0c15d7742bd88a6d8c20ed2d4a10bbd827dfe6156f6d5900f32393)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrBackupVaultArn")
    def attr_backup_vault_arn(self) -> builtins.str:
        '''An Amazon Resource Name (ARN) that uniquely identifies a backup vault;

        for example, ``arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault`` .

        :cloudformationAttribute: BackupVaultArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBackupVaultArn"))

    @builtins.property
    @jsii.member(jsii_name="attrBackupVaultName")
    def attr_backup_vault_name(self) -> builtins.str:
        '''The name of a logical container where backups are stored.

        Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created. They consist of lowercase and uppercase letters, numbers, and hyphens.

        :cloudformationAttribute: BackupVaultName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBackupVaultName"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="accessPolicy")
    def access_policy(self) -> typing.Any:
        '''A resource-based policy that is used to manage access permissions on the target backup vault.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-accesspolicy
        '''
        return typing.cast(typing.Any, jsii.get(self, "accessPolicy"))

    @access_policy.setter
    def access_policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c71a77681867800b0b78f8f2964e810b8ca4726133d11f521526c72057717e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="backupVaultName")
    def backup_vault_name(self) -> builtins.str:
        '''The name of a logical container where backups are stored.

        Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-backupvaultname
        '''
        return typing.cast(builtins.str, jsii.get(self, "backupVaultName"))

    @backup_vault_name.setter
    def backup_vault_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c56ff59ca47ea637fdabefb66a608321941d196bf6d2dceb2eea9346262e0f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupVaultName", value)

    @builtins.property
    @jsii.member(jsii_name="backupVaultTags")
    def backup_vault_tags(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        '''Metadata that you can assign to help organize the resources that you create.

        Each tag is a key-value pair.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-backupvaulttags
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "backupVaultTags"))

    @backup_vault_tags.setter
    def backup_vault_tags(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__599d86302cbf47a25e092c9a19c1a8a79975cf921a6c65ac57925c27df6ae78f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupVaultTags", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionKeyArn")
    def encryption_key_arn(self) -> typing.Optional[builtins.str]:
        '''A server-side encryption key you can specify to encrypt your backups from services that support full AWS Backup management;

        for example, ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` . If you specify a key, you must specify its ARN, not its alias. If you do not specify a key, AWS Backup creates a KMS key for you by default.

        To learn which AWS Backup services support full AWS Backup management and how AWS Backup handles encryption for backups from services that do not yet support full AWS Backup , see `Encryption for backups in AWS Backup <https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html>`_

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-encryptionkeyarn
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionKeyArn"))

    @encryption_key_arn.setter
    def encryption_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b7e5967a1c654d52c8f012c99b8973248dc38a07b13fd96c04780dc40269771)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="lockConfiguration")
    def lock_configuration(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupVault.LockConfigurationTypeProperty"]]:
        '''Configuration for `AWS Backup Vault Lock <https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-lockconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupVault.LockConfigurationTypeProperty"]], jsii.get(self, "lockConfiguration"))

    @lock_configuration.setter
    def lock_configuration(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupVault.LockConfigurationTypeProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b39c0ada04a33c8b6afdf71b70dc199ed3b70978eea3f5032cf3557509c9724a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lockConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="notifications")
    def notifications(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupVault.NotificationObjectTypeProperty"]]:
        '''The SNS event notifications for the specified backup vault.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-notifications
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupVault.NotificationObjectTypeProperty"]], jsii.get(self, "notifications"))

    @notifications.setter
    def notifications(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnBackupVault.NotificationObjectTypeProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db95d9f0c60d029a945ac4b6f7baa47e7ac2a37e13adf20171a0d39f8bdc96b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notifications", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-backup.CfnBackupVault.LockConfigurationTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "min_retention_days": "minRetentionDays",
            "changeable_for_days": "changeableForDays",
            "max_retention_days": "maxRetentionDays",
        },
    )
    class LockConfigurationTypeProperty:
        def __init__(
            self,
            *,
            min_retention_days: jsii.Number,
            changeable_for_days: typing.Optional[jsii.Number] = None,
            max_retention_days: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The ``LockConfigurationType`` property type specifies configuration for `AWS Backup Vault Lock <https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html>`_ .

            :param min_retention_days: The AWS Backup Vault Lock configuration that specifies the minimum retention period that the vault retains its recovery points. This setting can be useful if, for example, your organization's policies require you to retain certain data for at least seven years (2555 days). If this parameter is not specified, Vault Lock will not enforce a minimum retention period. If this parameter is specified, any backup or copy job to the vault must have a lifecycle policy with a retention period equal to or longer than the minimum retention period. If the job's retention period is shorter than that minimum retention period, then the vault fails that backup or copy job, and you should either modify your lifecycle settings or use a different vault. Recovery points already saved in the vault prior to Vault Lock are not affected.
            :param changeable_for_days: The AWS Backup Vault Lock configuration that specifies the number of days before the lock date. For example, setting ``ChangeableForDays`` to 30 on Jan. 1, 2022 at 8pm UTC will set the lock date to Jan. 31, 2022 at 8pm UTC. AWS Backup enforces a 72-hour cooling-off period before Vault Lock takes effect and becomes immutable. Therefore, you must set ``ChangeableForDays`` to 3 or greater. Before the lock date, you can delete Vault Lock from the vault using ``DeleteBackupVaultLockConfiguration`` or change the Vault Lock configuration using ``PutBackupVaultLockConfiguration`` . On and after the lock date, the Vault Lock becomes immutable and cannot be changed or deleted. If this parameter is not specified, you can delete Vault Lock from the vault using ``DeleteBackupVaultLockConfiguration`` or change the Vault Lock configuration using ``PutBackupVaultLockConfiguration`` at any time.
            :param max_retention_days: The AWS Backup Vault Lock configuration that specifies the maximum retention period that the vault retains its recovery points. This setting can be useful if, for example, your organization's policies require you to destroy certain data after retaining it for four years (1460 days). If this parameter is not included, Vault Lock does not enforce a maximum retention period on the recovery points in the vault. If this parameter is included without a value, Vault Lock will not enforce a maximum retention period. If this parameter is specified, any backup or copy job to the vault must have a lifecycle policy with a retention period equal to or shorter than the maximum retention period. If the job's retention period is longer than that maximum retention period, then the vault fails the backup or copy job, and you should either modify your lifecycle settings or use a different vault. Recovery points already saved in the vault prior to Vault Lock are not affected.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-lockconfigurationtype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_backup as backup
                
                lock_configuration_type_property = backup.CfnBackupVault.LockConfigurationTypeProperty(
                    min_retention_days=123,
                
                    # the properties below are optional
                    changeable_for_days=123,
                    max_retention_days=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__63d1c1b3afe7f894e31f359203445ad304faf4b932ff3ed2e929aba3bde86b49)
                check_type(argname="argument min_retention_days", value=min_retention_days, expected_type=type_hints["min_retention_days"])
                check_type(argname="argument changeable_for_days", value=changeable_for_days, expected_type=type_hints["changeable_for_days"])
                check_type(argname="argument max_retention_days", value=max_retention_days, expected_type=type_hints["max_retention_days"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "min_retention_days": min_retention_days,
            }
            if changeable_for_days is not None:
                self._values["changeable_for_days"] = changeable_for_days
            if max_retention_days is not None:
                self._values["max_retention_days"] = max_retention_days

        @builtins.property
        def min_retention_days(self) -> jsii.Number:
            '''The AWS Backup Vault Lock configuration that specifies the minimum retention period that the vault retains its recovery points.

            This setting can be useful if, for example, your organization's policies require you to retain certain data for at least seven years (2555 days).

            If this parameter is not specified, Vault Lock will not enforce a minimum retention period.

            If this parameter is specified, any backup or copy job to the vault must have a lifecycle policy with a retention period equal to or longer than the minimum retention period. If the job's retention period is shorter than that minimum retention period, then the vault fails that backup or copy job, and you should either modify your lifecycle settings or use a different vault. Recovery points already saved in the vault prior to Vault Lock are not affected.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-lockconfigurationtype.html#cfn-backup-backupvault-lockconfigurationtype-minretentiondays
            '''
            result = self._values.get("min_retention_days")
            assert result is not None, "Required property 'min_retention_days' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def changeable_for_days(self) -> typing.Optional[jsii.Number]:
            '''The AWS Backup Vault Lock configuration that specifies the number of days before the lock date.

            For example, setting ``ChangeableForDays`` to 30 on Jan. 1, 2022 at 8pm UTC will set the lock date to Jan. 31, 2022 at 8pm UTC.

            AWS Backup enforces a 72-hour cooling-off period before Vault Lock takes effect and becomes immutable. Therefore, you must set ``ChangeableForDays`` to 3 or greater.

            Before the lock date, you can delete Vault Lock from the vault using ``DeleteBackupVaultLockConfiguration`` or change the Vault Lock configuration using ``PutBackupVaultLockConfiguration`` . On and after the lock date, the Vault Lock becomes immutable and cannot be changed or deleted.

            If this parameter is not specified, you can delete Vault Lock from the vault using ``DeleteBackupVaultLockConfiguration`` or change the Vault Lock configuration using ``PutBackupVaultLockConfiguration`` at any time.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-lockconfigurationtype.html#cfn-backup-backupvault-lockconfigurationtype-changeablefordays
            '''
            result = self._values.get("changeable_for_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_retention_days(self) -> typing.Optional[jsii.Number]:
            '''The AWS Backup Vault Lock configuration that specifies the maximum retention period that the vault retains its recovery points.

            This setting can be useful if, for example, your organization's policies require you to destroy certain data after retaining it for four years (1460 days).

            If this parameter is not included, Vault Lock does not enforce a maximum retention period on the recovery points in the vault. If this parameter is included without a value, Vault Lock will not enforce a maximum retention period.

            If this parameter is specified, any backup or copy job to the vault must have a lifecycle policy with a retention period equal to or shorter than the maximum retention period. If the job's retention period is longer than that maximum retention period, then the vault fails the backup or copy job, and you should either modify your lifecycle settings or use a different vault. Recovery points already saved in the vault prior to Vault Lock are not affected.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-lockconfigurationtype.html#cfn-backup-backupvault-lockconfigurationtype-maxretentiondays
            '''
            result = self._values.get("max_retention_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LockConfigurationTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-backup.CfnBackupVault.NotificationObjectTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "backup_vault_events": "backupVaultEvents",
            "sns_topic_arn": "snsTopicArn",
        },
    )
    class NotificationObjectTypeProperty:
        def __init__(
            self,
            *,
            backup_vault_events: typing.Sequence[builtins.str],
            sns_topic_arn: builtins.str,
        ) -> None:
            '''Specifies an object containing SNS event notification properties for the target backup vault.

            :param backup_vault_events: An array of events that indicate the status of jobs to back up resources to the backup vault. For valid events, see `BackupVaultEvents <https://docs.aws.amazon.com/aws-backup/latest/devguide/API_PutBackupVaultNotifications.html#API_PutBackupVaultNotifications_RequestSyntax>`_ in the *AWS Backup API Guide* .
            :param sns_topic_arn: An ARN that uniquely identifies an Amazon Simple Notification Service (Amazon SNS) topic; for example, ``arn:aws:sns:us-west-2:111122223333:MyTopic`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-notificationobjecttype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_backup as backup
                
                notification_object_type_property = backup.CfnBackupVault.NotificationObjectTypeProperty(
                    backup_vault_events=["backupVaultEvents"],
                    sns_topic_arn="snsTopicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__114b4ccebf14c61a2b17165851e4fbe345051129158a340487a9f9a3f05da25b)
                check_type(argname="argument backup_vault_events", value=backup_vault_events, expected_type=type_hints["backup_vault_events"])
                check_type(argname="argument sns_topic_arn", value=sns_topic_arn, expected_type=type_hints["sns_topic_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "backup_vault_events": backup_vault_events,
                "sns_topic_arn": sns_topic_arn,
            }

        @builtins.property
        def backup_vault_events(self) -> typing.List[builtins.str]:
            '''An array of events that indicate the status of jobs to back up resources to the backup vault.

            For valid events, see `BackupVaultEvents <https://docs.aws.amazon.com/aws-backup/latest/devguide/API_PutBackupVaultNotifications.html#API_PutBackupVaultNotifications_RequestSyntax>`_ in the *AWS Backup API Guide* .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-notificationobjecttype.html#cfn-backup-backupvault-notificationobjecttype-backupvaultevents
            '''
            result = self._values.get("backup_vault_events")
            assert result is not None, "Required property 'backup_vault_events' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def sns_topic_arn(self) -> builtins.str:
            '''An ARN that uniquely identifies an Amazon Simple Notification Service (Amazon SNS) topic;

            for example, ``arn:aws:sns:us-west-2:111122223333:MyTopic`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-backupvault-notificationobjecttype.html#cfn-backup-backupvault-notificationobjecttype-snstopicarn
            '''
            result = self._values.get("sns_topic_arn")
            assert result is not None, "Required property 'sns_topic_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotificationObjectTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-backup.CfnBackupVaultProps",
    jsii_struct_bases=[],
    name_mapping={
        "backup_vault_name": "backupVaultName",
        "access_policy": "accessPolicy",
        "backup_vault_tags": "backupVaultTags",
        "encryption_key_arn": "encryptionKeyArn",
        "lock_configuration": "lockConfiguration",
        "notifications": "notifications",
    },
)
class CfnBackupVaultProps:
    def __init__(
        self,
        *,
        backup_vault_name: builtins.str,
        access_policy: typing.Any = None,
        backup_vault_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        encryption_key_arn: typing.Optional[builtins.str] = None,
        lock_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnBackupVault.LockConfigurationTypeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        notifications: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnBackupVault.NotificationObjectTypeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnBackupVault``.

        :param backup_vault_name: The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.
        :param access_policy: A resource-based policy that is used to manage access permissions on the target backup vault.
        :param backup_vault_tags: Metadata that you can assign to help organize the resources that you create. Each tag is a key-value pair.
        :param encryption_key_arn: A server-side encryption key you can specify to encrypt your backups from services that support full AWS Backup management; for example, ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` . If you specify a key, you must specify its ARN, not its alias. If you do not specify a key, AWS Backup creates a KMS key for you by default. To learn which AWS Backup services support full AWS Backup management and how AWS Backup handles encryption for backups from services that do not yet support full AWS Backup , see `Encryption for backups in AWS Backup <https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html>`_
        :param lock_configuration: Configuration for `AWS Backup Vault Lock <https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html>`_ .
        :param notifications: The SNS event notifications for the specified backup vault.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_backup as backup
            
            # access_policy: Any
            
            cfn_backup_vault_props = backup.CfnBackupVaultProps(
                backup_vault_name="backupVaultName",
            
                # the properties below are optional
                access_policy=access_policy,
                backup_vault_tags={
                    "backup_vault_tags_key": "backupVaultTags"
                },
                encryption_key_arn="encryptionKeyArn",
                lock_configuration=backup.CfnBackupVault.LockConfigurationTypeProperty(
                    min_retention_days=123,
            
                    # the properties below are optional
                    changeable_for_days=123,
                    max_retention_days=123
                ),
                notifications=backup.CfnBackupVault.NotificationObjectTypeProperty(
                    backup_vault_events=["backupVaultEvents"],
                    sns_topic_arn="snsTopicArn"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbdf05291db23d2caf60e2d70b4159d634f2bedc73d9fe37ee41bb25a24a9e55)
            check_type(argname="argument backup_vault_name", value=backup_vault_name, expected_type=type_hints["backup_vault_name"])
            check_type(argname="argument access_policy", value=access_policy, expected_type=type_hints["access_policy"])
            check_type(argname="argument backup_vault_tags", value=backup_vault_tags, expected_type=type_hints["backup_vault_tags"])
            check_type(argname="argument encryption_key_arn", value=encryption_key_arn, expected_type=type_hints["encryption_key_arn"])
            check_type(argname="argument lock_configuration", value=lock_configuration, expected_type=type_hints["lock_configuration"])
            check_type(argname="argument notifications", value=notifications, expected_type=type_hints["notifications"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "backup_vault_name": backup_vault_name,
        }
        if access_policy is not None:
            self._values["access_policy"] = access_policy
        if backup_vault_tags is not None:
            self._values["backup_vault_tags"] = backup_vault_tags
        if encryption_key_arn is not None:
            self._values["encryption_key_arn"] = encryption_key_arn
        if lock_configuration is not None:
            self._values["lock_configuration"] = lock_configuration
        if notifications is not None:
            self._values["notifications"] = notifications

    @builtins.property
    def backup_vault_name(self) -> builtins.str:
        '''The name of a logical container where backups are stored.

        Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. They consist of lowercase letters, numbers, and hyphens.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-backupvaultname
        '''
        result = self._values.get("backup_vault_name")
        assert result is not None, "Required property 'backup_vault_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_policy(self) -> typing.Any:
        '''A resource-based policy that is used to manage access permissions on the target backup vault.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-accesspolicy
        '''
        result = self._values.get("access_policy")
        return typing.cast(typing.Any, result)

    @builtins.property
    def backup_vault_tags(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        '''Metadata that you can assign to help organize the resources that you create.

        Each tag is a key-value pair.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-backupvaulttags
        '''
        result = self._values.get("backup_vault_tags")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def encryption_key_arn(self) -> typing.Optional[builtins.str]:
        '''A server-side encryption key you can specify to encrypt your backups from services that support full AWS Backup management;

        for example, ``arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`` . If you specify a key, you must specify its ARN, not its alias. If you do not specify a key, AWS Backup creates a KMS key for you by default.

        To learn which AWS Backup services support full AWS Backup management and how AWS Backup handles encryption for backups from services that do not yet support full AWS Backup , see `Encryption for backups in AWS Backup <https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html>`_

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-encryptionkeyarn
        '''
        result = self._values.get("encryption_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lock_configuration(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnBackupVault.LockConfigurationTypeProperty]]:
        '''Configuration for `AWS Backup Vault Lock <https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-lockconfiguration
        '''
        result = self._values.get("lock_configuration")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnBackupVault.LockConfigurationTypeProperty]], result)

    @builtins.property
    def notifications(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnBackupVault.NotificationObjectTypeProperty]]:
        '''The SNS event notifications for the specified backup vault.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html#cfn-backup-backupvault-notifications
        '''
        result = self._values.get("notifications")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnBackupVault.NotificationObjectTypeProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBackupVaultProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnFramework(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-backup.CfnFramework",
):
    '''A CloudFormation ``AWS::Backup::Framework``.

    Creates a framework with one or more controls. A framework is a collection of controls that you can use to evaluate your backup practices. By using pre-built customizable controls to define your policies, you can evaluate whether your backup practices comply with your policies and which resources are not yet in compliance.

    For a sample AWS CloudFormation template, see the `AWS Backup Developer Guide <https://docs.aws.amazon.com/aws-backup/latest/devguide/bam-cfn-integration.html#bam-cfn-frameworks-template>`_ .

    :cloudformationResource: AWS::Backup::Framework
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_backup as backup
        
        # control_scope: Any
        
        cfn_framework = backup.CfnFramework(self, "MyCfnFramework",
            framework_controls=[backup.CfnFramework.FrameworkControlProperty(
                control_name="controlName",
        
                # the properties below are optional
                control_input_parameters=[backup.CfnFramework.ControlInputParameterProperty(
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )],
                control_scope=control_scope
            )],
        
            # the properties below are optional
            framework_description="frameworkDescription",
            framework_name="frameworkName",
            framework_tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        framework_controls: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnFramework.FrameworkControlProperty", typing.Dict[builtins.str, typing.Any]]]]],
        framework_description: typing.Optional[builtins.str] = None,
        framework_name: typing.Optional[builtins.str] = None,
        framework_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Backup::Framework``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param framework_controls: Contains detailed information about all of the controls of a framework. Each framework must contain at least one control.
        :param framework_description: An optional description of the framework with a maximum 1,024 characters.
        :param framework_name: The unique name of a framework. This name is between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).
        :param framework_tags: A list of tags with which to tag your framework.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__825d958537f2a6be9e78e86f89e946b43c012fb159f6c7a60e3d1f6b6bb8ec45)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFrameworkProps(
            framework_controls=framework_controls,
            framework_description=framework_description,
            framework_name=framework_name,
            framework_tags=framework_tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1befd5d3aac330760979a0c05d9339d0d984bde78d506cd91e573904098799fc)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bb261cb62261a2673c1a1e2d56bb12fba1da8eb6abc14c639c6107ccd417747)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''The UTC time when you created your framework.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrDeploymentStatus")
    def attr_deployment_status(self) -> builtins.str:
        '''Depolyment status refers to whether your framework has completed deployment.

        This status is usually ``Completed`` , but might also be ``Create in progress`` or another status. For a list of statuses, see `Framework compliance status <https://docs.aws.amazon.com/aws-backup/latest/devguide/viewing-frameworks.html>`_ in the *Developer Guide* .

        :cloudformationAttribute: DeploymentStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDeploymentStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrFrameworkArn")
    def attr_framework_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of your framework.

        :cloudformationAttribute: FrameworkArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFrameworkArn"))

    @builtins.property
    @jsii.member(jsii_name="attrFrameworkStatus")
    def attr_framework_status(self) -> builtins.str:
        '''Framework status refers to whether you have turned on resource tracking for all of your resources.

        This status is ``Active`` when you turn on all resources the framework evaluates. For other statuses and steps to correct them, see `Framework compliance status <https://docs.aws.amazon.com/aws-backup/latest/devguide/viewing-frameworks.html>`_ in the *Developer Guide* .

        :cloudformationAttribute: FrameworkStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFrameworkStatus"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="frameworkControls")
    def framework_controls(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnFramework.FrameworkControlProperty"]]]:
        '''Contains detailed information about all of the controls of a framework.

        Each framework must contain at least one control.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#cfn-backup-framework-frameworkcontrols
        '''
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnFramework.FrameworkControlProperty"]]], jsii.get(self, "frameworkControls"))

    @framework_controls.setter
    def framework_controls(
        self,
        value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnFramework.FrameworkControlProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cdf2fe3743ee7a2f05c16cff11367c75b18107f549f681e41fd5dc1ba80129d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frameworkControls", value)

    @builtins.property
    @jsii.member(jsii_name="frameworkDescription")
    def framework_description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the framework with a maximum 1,024 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#cfn-backup-framework-frameworkdescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frameworkDescription"))

    @framework_description.setter
    def framework_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89059cc17b1b6f138564cec61ecca0b250b478032f26e17d8235ee857fac94ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frameworkDescription", value)

    @builtins.property
    @jsii.member(jsii_name="frameworkName")
    def framework_name(self) -> typing.Optional[builtins.str]:
        '''The unique name of a framework.

        This name is between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#cfn-backup-framework-frameworkname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frameworkName"))

    @framework_name.setter
    def framework_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fb5d8cf9105de9153d320b6efcdf6836b923b4584578b91320e76dcda44ba42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frameworkName", value)

    @builtins.property
    @jsii.member(jsii_name="frameworkTags")
    def framework_tags(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, _aws_cdk_core_f4b25747.CfnTag]]]]:
        '''A list of tags with which to tag your framework.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#cfn-backup-framework-frameworktags
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, _aws_cdk_core_f4b25747.CfnTag]]]], jsii.get(self, "frameworkTags"))

    @framework_tags.setter
    def framework_tags(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, _aws_cdk_core_f4b25747.CfnTag]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__265d6dd1f31e75f3c4ab4c16495e04ebc3bc544dfeb405728cbcdb9fbd17f7db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frameworkTags", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-backup.CfnFramework.ControlInputParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "parameter_name": "parameterName",
            "parameter_value": "parameterValue",
        },
    )
    class ControlInputParameterProperty:
        def __init__(
            self,
            *,
            parameter_name: builtins.str,
            parameter_value: builtins.str,
        ) -> None:
            '''A list of parameters for a control.

            A control can have zero, one, or more than one parameter. An example of a control with two parameters is: "backup plan frequency is at least ``daily`` and the retention period is at least ``1 year`` ". The first parameter is ``daily`` . The second parameter is ``1 year`` .

            :param parameter_name: The name of a parameter, for example, ``BackupPlanFrequency`` .
            :param parameter_value: The value of parameter, for example, ``hourly`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlinputparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_backup as backup
                
                control_input_parameter_property = backup.CfnFramework.ControlInputParameterProperty(
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e52ff9df2b78b58a83f662858aa26b0b08dee7fc305aae8ae3fc316ba25e9f7a)
                check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
                check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "parameter_name": parameter_name,
                "parameter_value": parameter_value,
            }

        @builtins.property
        def parameter_name(self) -> builtins.str:
            '''The name of a parameter, for example, ``BackupPlanFrequency`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlinputparameter.html#cfn-backup-framework-controlinputparameter-parametername
            '''
            result = self._values.get("parameter_name")
            assert result is not None, "Required property 'parameter_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameter_value(self) -> builtins.str:
            '''The value of parameter, for example, ``hourly`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlinputparameter.html#cfn-backup-framework-controlinputparameter-parametervalue
            '''
            result = self._values.get("parameter_value")
            assert result is not None, "Required property 'parameter_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ControlInputParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-backup.CfnFramework.ControlScopeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "compliance_resource_ids": "complianceResourceIds",
            "compliance_resource_types": "complianceResourceTypes",
            "tags": "tags",
        },
    )
    class ControlScopeProperty:
        def __init__(
            self,
            *,
            compliance_resource_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            compliance_resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
            tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A framework consists of one or more controls.

            Each control has its own control scope. The control scope can include one or more resource types, a combination of a tag key and value, or a combination of one resource type and one resource ID. If no scope is specified, evaluations for the rule are triggered when any resource in your recording group changes in configuration.
            .. epigraph::

               To set a control scope that includes all of a particular resource, leave the ``ControlScope`` empty or do not pass it when calling ``CreateFramework`` .

            :param compliance_resource_ids: The ID of the only AWS resource that you want your control scope to contain.
            :param compliance_resource_types: Describes whether the control scope includes one or more types of resources, such as ``EFS`` or ``RDS`` .
            :param tags: The tag key-value pair applied to those AWS resources that you want to trigger an evaluation for a rule. A maximum of one key-value pair can be provided. The tag value is optional, but it cannot be an empty string. The structure to assign a tag is: ``[{"Key":"string","Value":"string"}]`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlscope.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_backup as backup
                
                control_scope_property = backup.CfnFramework.ControlScopeProperty(
                    compliance_resource_ids=["complianceResourceIds"],
                    compliance_resource_types=["complianceResourceTypes"],
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4531714524260b8596db2b33da6630acf20c71447f8603b1576569d02d364715)
                check_type(argname="argument compliance_resource_ids", value=compliance_resource_ids, expected_type=type_hints["compliance_resource_ids"])
                check_type(argname="argument compliance_resource_types", value=compliance_resource_types, expected_type=type_hints["compliance_resource_types"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if compliance_resource_ids is not None:
                self._values["compliance_resource_ids"] = compliance_resource_ids
            if compliance_resource_types is not None:
                self._values["compliance_resource_types"] = compliance_resource_types
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def compliance_resource_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The ID of the only AWS resource that you want your control scope to contain.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlscope.html#cfn-backup-framework-controlscope-complianceresourceids
            '''
            result = self._values.get("compliance_resource_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def compliance_resource_types(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''Describes whether the control scope includes one or more types of resources, such as ``EFS`` or ``RDS`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlscope.html#cfn-backup-framework-controlscope-complianceresourcetypes
            '''
            result = self._values.get("compliance_resource_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]]:
            '''The tag key-value pair applied to those AWS resources that you want to trigger an evaluation for a rule.

            A maximum of one key-value pair can be provided. The tag value is optional, but it cannot be an empty string. The structure to assign a tag is: ``[{"Key":"string","Value":"string"}]`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-controlscope.html#cfn-backup-framework-controlscope-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ControlScopeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-backup.CfnFramework.FrameworkControlProperty",
        jsii_struct_bases=[],
        name_mapping={
            "control_name": "controlName",
            "control_input_parameters": "controlInputParameters",
            "control_scope": "controlScope",
        },
    )
    class FrameworkControlProperty:
        def __init__(
            self,
            *,
            control_name: builtins.str,
            control_input_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnFramework.ControlInputParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            control_scope: typing.Any = None,
        ) -> None:
            '''Contains detailed information about all of the controls of a framework.

            Each framework must contain at least one control.

            :param control_name: The name of a control. This name is between 1 and 256 characters.
            :param control_input_parameters: A list of ``ParameterName`` and ``ParameterValue`` pairs.
            :param control_scope: The scope of a control. The control scope defines what the control will evaluate. Three examples of control scopes are: a specific backup plan, all backup plans with a specific tag, or all backup plans. For more information, see ```ControlScope`` . <https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ControlScope.html>`_

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-frameworkcontrol.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_backup as backup
                
                # control_scope: Any
                
                framework_control_property = backup.CfnFramework.FrameworkControlProperty(
                    control_name="controlName",
                
                    # the properties below are optional
                    control_input_parameters=[backup.CfnFramework.ControlInputParameterProperty(
                        parameter_name="parameterName",
                        parameter_value="parameterValue"
                    )],
                    control_scope=control_scope
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__03b0b19e58fb272ecebfc944079a5220ecd6c2620354a259e9f0c0ab8a16764b)
                check_type(argname="argument control_name", value=control_name, expected_type=type_hints["control_name"])
                check_type(argname="argument control_input_parameters", value=control_input_parameters, expected_type=type_hints["control_input_parameters"])
                check_type(argname="argument control_scope", value=control_scope, expected_type=type_hints["control_scope"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "control_name": control_name,
            }
            if control_input_parameters is not None:
                self._values["control_input_parameters"] = control_input_parameters
            if control_scope is not None:
                self._values["control_scope"] = control_scope

        @builtins.property
        def control_name(self) -> builtins.str:
            '''The name of a control.

            This name is between 1 and 256 characters.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-frameworkcontrol.html#cfn-backup-framework-frameworkcontrol-controlname
            '''
            result = self._values.get("control_name")
            assert result is not None, "Required property 'control_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def control_input_parameters(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnFramework.ControlInputParameterProperty"]]]]:
            '''A list of ``ParameterName`` and ``ParameterValue`` pairs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-frameworkcontrol.html#cfn-backup-framework-frameworkcontrol-controlinputparameters
            '''
            result = self._values.get("control_input_parameters")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnFramework.ControlInputParameterProperty"]]]], result)

        @builtins.property
        def control_scope(self) -> typing.Any:
            '''The scope of a control.

            The control scope defines what the control will evaluate. Three examples of control scopes are: a specific backup plan, all backup plans with a specific tag, or all backup plans. For more information, see ```ControlScope`` . <https://docs.aws.amazon.com/aws-backup/latest/devguide/API_ControlScope.html>`_

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-framework-frameworkcontrol.html#cfn-backup-framework-frameworkcontrol-controlscope
            '''
            result = self._values.get("control_scope")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FrameworkControlProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-backup.CfnFrameworkProps",
    jsii_struct_bases=[],
    name_mapping={
        "framework_controls": "frameworkControls",
        "framework_description": "frameworkDescription",
        "framework_name": "frameworkName",
        "framework_tags": "frameworkTags",
    },
)
class CfnFrameworkProps:
    def __init__(
        self,
        *,
        framework_controls: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnFramework.FrameworkControlProperty, typing.Dict[builtins.str, typing.Any]]]]],
        framework_description: typing.Optional[builtins.str] = None,
        framework_name: typing.Optional[builtins.str] = None,
        framework_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFramework``.

        :param framework_controls: Contains detailed information about all of the controls of a framework. Each framework must contain at least one control.
        :param framework_description: An optional description of the framework with a maximum 1,024 characters.
        :param framework_name: The unique name of a framework. This name is between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).
        :param framework_tags: A list of tags with which to tag your framework.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_backup as backup
            
            # control_scope: Any
            
            cfn_framework_props = backup.CfnFrameworkProps(
                framework_controls=[backup.CfnFramework.FrameworkControlProperty(
                    control_name="controlName",
            
                    # the properties below are optional
                    control_input_parameters=[backup.CfnFramework.ControlInputParameterProperty(
                        parameter_name="parameterName",
                        parameter_value="parameterValue"
                    )],
                    control_scope=control_scope
                )],
            
                # the properties below are optional
                framework_description="frameworkDescription",
                framework_name="frameworkName",
                framework_tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cb80049cdda91bb4a7be90784452a3e2674eb27d1f8838437181c850788366a)
            check_type(argname="argument framework_controls", value=framework_controls, expected_type=type_hints["framework_controls"])
            check_type(argname="argument framework_description", value=framework_description, expected_type=type_hints["framework_description"])
            check_type(argname="argument framework_name", value=framework_name, expected_type=type_hints["framework_name"])
            check_type(argname="argument framework_tags", value=framework_tags, expected_type=type_hints["framework_tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "framework_controls": framework_controls,
        }
        if framework_description is not None:
            self._values["framework_description"] = framework_description
        if framework_name is not None:
            self._values["framework_name"] = framework_name
        if framework_tags is not None:
            self._values["framework_tags"] = framework_tags

    @builtins.property
    def framework_controls(
        self,
    ) -> typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnFramework.FrameworkControlProperty]]]:
        '''Contains detailed information about all of the controls of a framework.

        Each framework must contain at least one control.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#cfn-backup-framework-frameworkcontrols
        '''
        result = self._values.get("framework_controls")
        assert result is not None, "Required property 'framework_controls' is missing"
        return typing.cast(typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnFramework.FrameworkControlProperty]]], result)

    @builtins.property
    def framework_description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the framework with a maximum 1,024 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#cfn-backup-framework-frameworkdescription
        '''
        result = self._values.get("framework_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def framework_name(self) -> typing.Optional[builtins.str]:
        '''The unique name of a framework.

        This name is between 1 and 256 characters, starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#cfn-backup-framework-frameworkname
        '''
        result = self._values.get("framework_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def framework_tags(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, _aws_cdk_core_f4b25747.CfnTag]]]]:
        '''A list of tags with which to tag your framework.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-framework.html#cfn-backup-framework-frameworktags
        '''
        result = self._values.get("framework_tags")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, _aws_cdk_core_f4b25747.CfnTag]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFrameworkProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnReportPlan(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-backup.CfnReportPlan",
):
    '''A CloudFormation ``AWS::Backup::ReportPlan``.

    Creates a report plan. A report plan is a document that contains information about the contents of the report and where AWS Backup will deliver it.

    If you call ``CreateReportPlan`` with a plan that already exists, you receive an ``AlreadyExistsException`` exception.

    For a sample AWS CloudFormation template, see the `AWS Backup Developer Guide <https://docs.aws.amazon.com/aws-backup/latest/devguide/assigning-resources.html#assigning-resources-cfn>`_ .

    :cloudformationResource: AWS::Backup::ReportPlan
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_backup as backup
        
        # report_delivery_channel: Any
        # report_setting: Any
        
        cfn_report_plan = backup.CfnReportPlan(self, "MyCfnReportPlan",
            report_delivery_channel=report_delivery_channel,
            report_setting=report_setting,
        
            # the properties below are optional
            report_plan_description="reportPlanDescription",
            report_plan_name="reportPlanName",
            report_plan_tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        report_delivery_channel: typing.Any,
        report_setting: typing.Any,
        report_plan_description: typing.Optional[builtins.str] = None,
        report_plan_name: typing.Optional[builtins.str] = None,
        report_plan_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Backup::ReportPlan``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param report_delivery_channel: Contains information about where and how to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.
        :param report_setting: Identifies the report template for the report. Reports are built using a report template. The report templates are:. ``RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT`` If the report template is ``RESOURCE_COMPLIANCE_REPORT`` or ``CONTROL_COMPLIANCE_REPORT`` , this API resource also describes the report coverage by AWS Regions and frameworks.
        :param report_plan_description: An optional description of the report plan with a maximum 1,024 characters.
        :param report_plan_name: The unique name of the report plan. This name is between 1 and 256 characters starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).
        :param report_plan_tags: A list of tags to tag your report plan.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__390f524888340f40e5af7ec4fb30a9c65b2b2cae5e58e9e91929c1e6495ce2ba)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnReportPlanProps(
            report_delivery_channel=report_delivery_channel,
            report_setting=report_setting,
            report_plan_description=report_plan_description,
            report_plan_name=report_plan_name,
            report_plan_tags=report_plan_tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db5f0d91e3c60eb327fd93d6aa938729558004a367ee968adbb55a74779c23c5)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03c8471b5d5b1ab9b4d92aea5dbc5d69ac7f68bd98877249f3852e8af3b81f78)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrReportPlanArn")
    def attr_report_plan_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of your report plan.

        :cloudformationAttribute: ReportPlanArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrReportPlanArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="reportDeliveryChannel")
    def report_delivery_channel(self) -> typing.Any:
        '''Contains information about where and how to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportdeliverychannel
        '''
        return typing.cast(typing.Any, jsii.get(self, "reportDeliveryChannel"))

    @report_delivery_channel.setter
    def report_delivery_channel(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ce7706b39b2db939bbbb6cd7996caeeff8d947564992d1e2f7b6e169c37dbec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reportDeliveryChannel", value)

    @builtins.property
    @jsii.member(jsii_name="reportSetting")
    def report_setting(self) -> typing.Any:
        '''Identifies the report template for the report. Reports are built using a report template. The report templates are:.

        ``RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT``

        If the report template is ``RESOURCE_COMPLIANCE_REPORT`` or ``CONTROL_COMPLIANCE_REPORT`` , this API resource also describes the report coverage by AWS Regions and frameworks.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportsetting
        '''
        return typing.cast(typing.Any, jsii.get(self, "reportSetting"))

    @report_setting.setter
    def report_setting(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a1f5e7e14384bfe189f6c12da3dc35e2f4a6e267f24aeeff8df66668e690eff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reportSetting", value)

    @builtins.property
    @jsii.member(jsii_name="reportPlanDescription")
    def report_plan_description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the report plan with a maximum 1,024 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportplandescription
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "reportPlanDescription"))

    @report_plan_description.setter
    def report_plan_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13e056d728bb403ec0b42ee4744cf6e8bfdf32ae4defa39dfae3ca6070302f59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reportPlanDescription", value)

    @builtins.property
    @jsii.member(jsii_name="reportPlanName")
    def report_plan_name(self) -> typing.Optional[builtins.str]:
        '''The unique name of the report plan.

        This name is between 1 and 256 characters starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportplanname
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "reportPlanName"))

    @report_plan_name.setter
    def report_plan_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__406b2829cb701e4dfd685f17f2579d51b232b4ab433cb05d8fed0e88955e78c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reportPlanName", value)

    @builtins.property
    @jsii.member(jsii_name="reportPlanTags")
    def report_plan_tags(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, _aws_cdk_core_f4b25747.CfnTag]]]]:
        '''A list of tags to tag your report plan.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportplantags
        '''
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, _aws_cdk_core_f4b25747.CfnTag]]]], jsii.get(self, "reportPlanTags"))

    @report_plan_tags.setter
    def report_plan_tags(
        self,
        value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, _aws_cdk_core_f4b25747.CfnTag]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__610ab7422f09eedcb67cf4dbda8dc7b5050833b36bd6b9245ee51aeddd623d5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reportPlanTags", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-backup.CfnReportPlan.ReportDeliveryChannelProperty",
        jsii_struct_bases=[],
        name_mapping={
            "s3_bucket_name": "s3BucketName",
            "formats": "formats",
            "s3_key_prefix": "s3KeyPrefix",
        },
    )
    class ReportDeliveryChannelProperty:
        def __init__(
            self,
            *,
            s3_bucket_name: builtins.str,
            formats: typing.Optional[typing.Sequence[builtins.str]] = None,
            s3_key_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information from your report plan about where to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.

            :param s3_bucket_name: The unique name of the S3 bucket that receives your reports.
            :param formats: A list of the format of your reports: ``CSV`` , ``JSON`` , or both. If not specified, the default format is ``CSV`` .
            :param s3_key_prefix: The prefix for where AWS Backup Audit Manager delivers your reports to Amazon S3. The prefix is this part of the following path: s3://your-bucket-name/ ``prefix`` /Backup/us-west-2/year/month/day/report-name. If not specified, there is no prefix.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportdeliverychannel.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_backup as backup
                
                report_delivery_channel_property = backup.CfnReportPlan.ReportDeliveryChannelProperty(
                    s3_bucket_name="s3BucketName",
                
                    # the properties below are optional
                    formats=["formats"],
                    s3_key_prefix="s3KeyPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__89b9196515d065d7820b83d542ac81ae5ca3637423a638149f5deae68cd45055)
                check_type(argname="argument s3_bucket_name", value=s3_bucket_name, expected_type=type_hints["s3_bucket_name"])
                check_type(argname="argument formats", value=formats, expected_type=type_hints["formats"])
                check_type(argname="argument s3_key_prefix", value=s3_key_prefix, expected_type=type_hints["s3_key_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3_bucket_name": s3_bucket_name,
            }
            if formats is not None:
                self._values["formats"] = formats
            if s3_key_prefix is not None:
                self._values["s3_key_prefix"] = s3_key_prefix

        @builtins.property
        def s3_bucket_name(self) -> builtins.str:
            '''The unique name of the S3 bucket that receives your reports.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportdeliverychannel.html#cfn-backup-reportplan-reportdeliverychannel-s3bucketname
            '''
            result = self._values.get("s3_bucket_name")
            assert result is not None, "Required property 's3_bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def formats(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of the format of your reports: ``CSV`` , ``JSON`` , or both.

            If not specified, the default format is ``CSV`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportdeliverychannel.html#cfn-backup-reportplan-reportdeliverychannel-formats
            '''
            result = self._values.get("formats")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def s3_key_prefix(self) -> typing.Optional[builtins.str]:
            '''The prefix for where AWS Backup Audit Manager delivers your reports to Amazon S3.

            The prefix is this part of the following path: s3://your-bucket-name/ ``prefix`` /Backup/us-west-2/year/month/day/report-name. If not specified, there is no prefix.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportdeliverychannel.html#cfn-backup-reportplan-reportdeliverychannel-s3keyprefix
            '''
            result = self._values.get("s3_key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReportDeliveryChannelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-backup.CfnReportPlan.ReportSettingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "report_template": "reportTemplate",
            "accounts": "accounts",
            "framework_arns": "frameworkArns",
            "organization_units": "organizationUnits",
            "regions": "regions",
        },
    )
    class ReportSettingProperty:
        def __init__(
            self,
            *,
            report_template: builtins.str,
            accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
            framework_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
            organization_units: typing.Optional[typing.Sequence[builtins.str]] = None,
            regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Contains detailed information about a report setting.

            :param report_template: Identifies the report template for the report. Reports are built using a report template. The report templates are:. ``RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT``
            :param accounts: These are the accounts to be included in the report.
            :param framework_arns: The Amazon Resource Names (ARNs) of the frameworks a report covers.
            :param organization_units: These are the Organizational Units to be included in the report.
            :param regions: These are the Regions to be included in the report.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportsetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_backup as backup
                
                report_setting_property = backup.CfnReportPlan.ReportSettingProperty(
                    report_template="reportTemplate",
                
                    # the properties below are optional
                    accounts=["accounts"],
                    framework_arns=["frameworkArns"],
                    organization_units=["organizationUnits"],
                    regions=["regions"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b391517c32a8e2a6ddf10ce1a41e6a1b3391208f50c3fabf1d50c89e80536082)
                check_type(argname="argument report_template", value=report_template, expected_type=type_hints["report_template"])
                check_type(argname="argument accounts", value=accounts, expected_type=type_hints["accounts"])
                check_type(argname="argument framework_arns", value=framework_arns, expected_type=type_hints["framework_arns"])
                check_type(argname="argument organization_units", value=organization_units, expected_type=type_hints["organization_units"])
                check_type(argname="argument regions", value=regions, expected_type=type_hints["regions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "report_template": report_template,
            }
            if accounts is not None:
                self._values["accounts"] = accounts
            if framework_arns is not None:
                self._values["framework_arns"] = framework_arns
            if organization_units is not None:
                self._values["organization_units"] = organization_units
            if regions is not None:
                self._values["regions"] = regions

        @builtins.property
        def report_template(self) -> builtins.str:
            '''Identifies the report template for the report. Reports are built using a report template. The report templates are:.

            ``RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT``

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportsetting.html#cfn-backup-reportplan-reportsetting-reporttemplate
            '''
            result = self._values.get("report_template")
            assert result is not None, "Required property 'report_template' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def accounts(self) -> typing.Optional[typing.List[builtins.str]]:
            '''These are the accounts to be included in the report.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportsetting.html#cfn-backup-reportplan-reportsetting-accounts
            '''
            result = self._values.get("accounts")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def framework_arns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The Amazon Resource Names (ARNs) of the frameworks a report covers.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportsetting.html#cfn-backup-reportplan-reportsetting-frameworkarns
            '''
            result = self._values.get("framework_arns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def organization_units(self) -> typing.Optional[typing.List[builtins.str]]:
            '''These are the Organizational Units to be included in the report.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportsetting.html#cfn-backup-reportplan-reportsetting-organizationunits
            '''
            result = self._values.get("organization_units")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def regions(self) -> typing.Optional[typing.List[builtins.str]]:
            '''These are the Regions to be included in the report.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-backup-reportplan-reportsetting.html#cfn-backup-reportplan-reportsetting-regions
            '''
            result = self._values.get("regions")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReportSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-backup.CfnReportPlanProps",
    jsii_struct_bases=[],
    name_mapping={
        "report_delivery_channel": "reportDeliveryChannel",
        "report_setting": "reportSetting",
        "report_plan_description": "reportPlanDescription",
        "report_plan_name": "reportPlanName",
        "report_plan_tags": "reportPlanTags",
    },
)
class CfnReportPlanProps:
    def __init__(
        self,
        *,
        report_delivery_channel: typing.Any,
        report_setting: typing.Any,
        report_plan_description: typing.Optional[builtins.str] = None,
        report_plan_name: typing.Optional[builtins.str] = None,
        report_plan_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnReportPlan``.

        :param report_delivery_channel: Contains information about where and how to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.
        :param report_setting: Identifies the report template for the report. Reports are built using a report template. The report templates are:. ``RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT`` If the report template is ``RESOURCE_COMPLIANCE_REPORT`` or ``CONTROL_COMPLIANCE_REPORT`` , this API resource also describes the report coverage by AWS Regions and frameworks.
        :param report_plan_description: An optional description of the report plan with a maximum 1,024 characters.
        :param report_plan_name: The unique name of the report plan. This name is between 1 and 256 characters starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).
        :param report_plan_tags: A list of tags to tag your report plan.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_backup as backup
            
            # report_delivery_channel: Any
            # report_setting: Any
            
            cfn_report_plan_props = backup.CfnReportPlanProps(
                report_delivery_channel=report_delivery_channel,
                report_setting=report_setting,
            
                # the properties below are optional
                report_plan_description="reportPlanDescription",
                report_plan_name="reportPlanName",
                report_plan_tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2efd0635581bb86b9b16facdfa93569f20269948d1e14439d8354cf9522a99c0)
            check_type(argname="argument report_delivery_channel", value=report_delivery_channel, expected_type=type_hints["report_delivery_channel"])
            check_type(argname="argument report_setting", value=report_setting, expected_type=type_hints["report_setting"])
            check_type(argname="argument report_plan_description", value=report_plan_description, expected_type=type_hints["report_plan_description"])
            check_type(argname="argument report_plan_name", value=report_plan_name, expected_type=type_hints["report_plan_name"])
            check_type(argname="argument report_plan_tags", value=report_plan_tags, expected_type=type_hints["report_plan_tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "report_delivery_channel": report_delivery_channel,
            "report_setting": report_setting,
        }
        if report_plan_description is not None:
            self._values["report_plan_description"] = report_plan_description
        if report_plan_name is not None:
            self._values["report_plan_name"] = report_plan_name
        if report_plan_tags is not None:
            self._values["report_plan_tags"] = report_plan_tags

    @builtins.property
    def report_delivery_channel(self) -> typing.Any:
        '''Contains information about where and how to deliver your reports, specifically your Amazon S3 bucket name, S3 key prefix, and the formats of your reports.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportdeliverychannel
        '''
        result = self._values.get("report_delivery_channel")
        assert result is not None, "Required property 'report_delivery_channel' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def report_setting(self) -> typing.Any:
        '''Identifies the report template for the report. Reports are built using a report template. The report templates are:.

        ``RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT``

        If the report template is ``RESOURCE_COMPLIANCE_REPORT`` or ``CONTROL_COMPLIANCE_REPORT`` , this API resource also describes the report coverage by AWS Regions and frameworks.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportsetting
        '''
        result = self._values.get("report_setting")
        assert result is not None, "Required property 'report_setting' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def report_plan_description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the report plan with a maximum 1,024 characters.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportplandescription
        '''
        result = self._values.get("report_plan_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def report_plan_name(self) -> typing.Optional[builtins.str]:
        '''The unique name of the report plan.

        This name is between 1 and 256 characters starting with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores (_).

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportplanname
        '''
        result = self._values.get("report_plan_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def report_plan_tags(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, _aws_cdk_core_f4b25747.CfnTag]]]]:
        '''A list of tags to tag your report plan.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-reportplan.html#cfn-backup-reportplan-reportplantags
        '''
        result = self._values.get("report_plan_tags")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, _aws_cdk_core_f4b25747.CfnTag]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReportPlanProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@aws-cdk/aws-backup.IBackupPlan")
class IBackupPlan(_aws_cdk_core_f4b25747.IResource, typing_extensions.Protocol):
    '''A backup plan.'''

    @builtins.property
    @jsii.member(jsii_name="backupPlanId")
    def backup_plan_id(self) -> builtins.str:
        '''The identifier of the backup plan.

        :attribute: true
        '''
        ...


class _IBackupPlanProxy(
    jsii.proxy_for(_aws_cdk_core_f4b25747.IResource), # type: ignore[misc]
):
    '''A backup plan.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-backup.IBackupPlan"

    @builtins.property
    @jsii.member(jsii_name="backupPlanId")
    def backup_plan_id(self) -> builtins.str:
        '''The identifier of the backup plan.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "backupPlanId"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBackupPlan).__jsii_proxy_class__ = lambda : _IBackupPlanProxy


@jsii.interface(jsii_type="@aws-cdk/aws-backup.IBackupVault")
class IBackupVault(_aws_cdk_core_f4b25747.IResource, typing_extensions.Protocol):
    '''A backup vault.'''

    @builtins.property
    @jsii.member(jsii_name="backupVaultArn")
    def backup_vault_arn(self) -> builtins.str:
        '''The ARN of the backup vault.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="backupVaultName")
    def backup_vault_name(self) -> builtins.str:
        '''The name of a logical container where backups are stored.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _aws_cdk_aws_iam_940a1ce0.IGrantable,
        *actions: builtins.str,
    ) -> _aws_cdk_aws_iam_940a1ce0.Grant:
        '''Grant the actions defined in actions to the given grantee on this backup vault.

        :param grantee: -
        :param actions: -
        '''
        ...


class _IBackupVaultProxy(
    jsii.proxy_for(_aws_cdk_core_f4b25747.IResource), # type: ignore[misc]
):
    '''A backup vault.'''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-backup.IBackupVault"

    @builtins.property
    @jsii.member(jsii_name="backupVaultArn")
    def backup_vault_arn(self) -> builtins.str:
        '''The ARN of the backup vault.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "backupVaultArn"))

    @builtins.property
    @jsii.member(jsii_name="backupVaultName")
    def backup_vault_name(self) -> builtins.str:
        '''The name of a logical container where backups are stored.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "backupVaultName"))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _aws_cdk_aws_iam_940a1ce0.IGrantable,
        *actions: builtins.str,
    ) -> _aws_cdk_aws_iam_940a1ce0.Grant:
        '''Grant the actions defined in actions to the given grantee on this backup vault.

        :param grantee: -
        :param actions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9be7cb9a72282277bdb1999318759995687e0261947e074734bf3563ee32879c)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_aws_cdk_aws_iam_940a1ce0.Grant, jsii.invoke(self, "grant", [grantee, *actions]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBackupVault).__jsii_proxy_class__ = lambda : _IBackupVaultProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-backup.TagCondition",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value", "operation": "operation"},
)
class TagCondition:
    def __init__(
        self,
        *,
        key: builtins.str,
        value: builtins.str,
        operation: typing.Optional["TagOperation"] = None,
    ) -> None:
        '''A tag condition.

        :param key: The key in a key-value pair. For example, in ``"ec2:ResourceTag/Department": "accounting"``, ``ec2:ResourceTag/Department`` is the key.
        :param value: The value in a key-value pair. For example, in ``"ec2:ResourceTag/Department": "accounting"``, ``accounting`` is the value.
        :param operation: An operation that is applied to a key-value pair used to filter resources in a selection. Default: STRING_EQUALS

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_backup as backup
            
            tag_condition = backup.TagCondition(
                key="key",
                value="value",
            
                # the properties below are optional
                operation=backup.TagOperation.STRING_EQUALS
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b4d78dc0770c848384558d42a4d12762945fd9e1e21688cea4aed7750c53bef)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument operation", value=operation, expected_type=type_hints["operation"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "value": value,
        }
        if operation is not None:
            self._values["operation"] = operation

    @builtins.property
    def key(self) -> builtins.str:
        '''The key in a key-value pair.

        For example, in ``"ec2:ResourceTag/Department": "accounting"``,
        ``ec2:ResourceTag/Department`` is the key.
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The value in a key-value pair.

        For example, in ``"ec2:ResourceTag/Department": "accounting"``,
        ``accounting`` is the value.
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operation(self) -> typing.Optional["TagOperation"]:
        '''An operation that is applied to a key-value pair used to filter resources in a selection.

        :default: STRING_EQUALS
        '''
        result = self._values.get("operation")
        return typing.cast(typing.Optional["TagOperation"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TagCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/aws-backup.TagOperation")
class TagOperation(enum.Enum):
    '''An operation that is applied to a key-value pair.'''

    STRING_EQUALS = "STRING_EQUALS"
    '''StringEquals.'''
    DUMMY = "DUMMY"
    '''Dummy member.'''


@jsii.implements(IBackupPlan)
class BackupPlan(
    _aws_cdk_core_f4b25747.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-backup.BackupPlan",
):
    '''A backup plan.

    :exampleMetadata: infused

    Example::

        # Daily, weekly and monthly with 5 year retention
        plan = backup.BackupPlan.daily_weekly_monthly5_year_retention(self, "Plan")
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        backup_plan_name: typing.Optional[builtins.str] = None,
        backup_plan_rules: typing.Optional[typing.Sequence[BackupPlanRule]] = None,
        backup_vault: typing.Optional[IBackupVault] = None,
        windows_vss: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param backup_plan_name: The display name of the backup plan. Default: - A CDK generated name
        :param backup_plan_rules: Rules for the backup plan. Use ``addRule()`` to add rules after instantiation. Default: - use ``addRule()`` to add rules
        :param backup_vault: The backup vault where backups are stored. Default: - use the vault defined at the rule level. If not defined a new common vault for the plan will be created
        :param windows_vss: Enable Windows VSS backup. Default: false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3996e8ae85f0f31ff5212254e44d9f3a1483fbc4a57606abacb1ac2648649b22)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = BackupPlanProps(
            backup_plan_name=backup_plan_name,
            backup_plan_rules=backup_plan_rules,
            backup_vault=backup_vault,
            windows_vss=windows_vss,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="daily35DayRetention")
    @builtins.classmethod
    def daily35_day_retention(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        backup_vault: typing.Optional[IBackupVault] = None,
    ) -> "BackupPlan":
        '''Daily with 35 day retention.

        :param scope: -
        :param id: -
        :param backup_vault: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f1f682073df85df9c67b8b68240013c0e22667c386b2c473c7c560dcb4061c2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument backup_vault", value=backup_vault, expected_type=type_hints["backup_vault"])
        return typing.cast("BackupPlan", jsii.sinvoke(cls, "daily35DayRetention", [scope, id, backup_vault]))

    @jsii.member(jsii_name="dailyMonthly1YearRetention")
    @builtins.classmethod
    def daily_monthly1_year_retention(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        backup_vault: typing.Optional[IBackupVault] = None,
    ) -> "BackupPlan":
        '''Daily and monthly with 1 year retention.

        :param scope: -
        :param id: -
        :param backup_vault: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a593977513729bb7363f767a1233ed191bdcc5af5075ac929e0cd79b03da51d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument backup_vault", value=backup_vault, expected_type=type_hints["backup_vault"])
        return typing.cast("BackupPlan", jsii.sinvoke(cls, "dailyMonthly1YearRetention", [scope, id, backup_vault]))

    @jsii.member(jsii_name="dailyWeeklyMonthly5YearRetention")
    @builtins.classmethod
    def daily_weekly_monthly5_year_retention(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        backup_vault: typing.Optional[IBackupVault] = None,
    ) -> "BackupPlan":
        '''Daily, weekly and monthly with 5 year retention.

        :param scope: -
        :param id: -
        :param backup_vault: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dbf7bbf30071fe58d8579890c51492755b2c0caacd1df612911764d3b833666)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument backup_vault", value=backup_vault, expected_type=type_hints["backup_vault"])
        return typing.cast("BackupPlan", jsii.sinvoke(cls, "dailyWeeklyMonthly5YearRetention", [scope, id, backup_vault]))

    @jsii.member(jsii_name="dailyWeeklyMonthly7YearRetention")
    @builtins.classmethod
    def daily_weekly_monthly7_year_retention(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        backup_vault: typing.Optional[IBackupVault] = None,
    ) -> "BackupPlan":
        '''Daily, weekly and monthly with 7 year retention.

        :param scope: -
        :param id: -
        :param backup_vault: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd9e5ee6394bf689b4d9aefda6d363bb8b2685dd53fdd5cb1586cd316800eee2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument backup_vault", value=backup_vault, expected_type=type_hints["backup_vault"])
        return typing.cast("BackupPlan", jsii.sinvoke(cls, "dailyWeeklyMonthly7YearRetention", [scope, id, backup_vault]))

    @jsii.member(jsii_name="fromBackupPlanId")
    @builtins.classmethod
    def from_backup_plan_id(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        backup_plan_id: builtins.str,
    ) -> IBackupPlan:
        '''Import an existing backup plan.

        :param scope: -
        :param id: -
        :param backup_plan_id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d413ea15c25639b7e5ee6e75637b32483799be62ab2f38a1f00725dec454b4a2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument backup_plan_id", value=backup_plan_id, expected_type=type_hints["backup_plan_id"])
        return typing.cast(IBackupPlan, jsii.sinvoke(cls, "fromBackupPlanId", [scope, id, backup_plan_id]))

    @jsii.member(jsii_name="addRule")
    def add_rule(self, rule: BackupPlanRule) -> None:
        '''Adds a rule to a plan.

        :param rule: the rule to add.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__beadee2174d8e3589491028eb012ae8cda0cee5f1139a97fed65ba6ba0a808a1)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
        return typing.cast(None, jsii.invoke(self, "addRule", [rule]))

    @jsii.member(jsii_name="addSelection")
    def add_selection(
        self,
        id: builtins.str,
        *,
        resources: typing.Sequence[BackupResource],
        allow_restores: typing.Optional[builtins.bool] = None,
        backup_selection_name: typing.Optional[builtins.str] = None,
        role: typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole] = None,
    ) -> BackupSelection:
        '''Adds a selection to this plan.

        :param id: -
        :param resources: The resources to backup. Use the helper static methods defined on ``BackupResource``.
        :param allow_restores: Whether to automatically give restores permissions to the role that AWS Backup uses. If ``true``, the ``AWSBackupServiceRolePolicyForRestores`` managed policy will be attached to the role. Default: false
        :param backup_selection_name: The name for this selection. Default: - a CDK generated name
        :param role: The role that AWS Backup uses to authenticate when backuping or restoring the resources. The ``AWSBackupServiceRolePolicyForBackup`` managed policy will be attached to this role. Default: - a new role will be created
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d3bb42ef17a6534442b682780cc29b28c9cdbe725c5cd104654e2b214646cee)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = BackupSelectionOptions(
            resources=resources,
            allow_restores=allow_restores,
            backup_selection_name=backup_selection_name,
            role=role,
        )

        return typing.cast(BackupSelection, jsii.invoke(self, "addSelection", [id, options]))

    @jsii.member(jsii_name="validate")
    def _validate(self) -> typing.List[builtins.str]:
        '''Validate the current construct.

        This method can be implemented by derived constructs in order to perform
        validation logic. It is called on all constructs before synthesis.
        '''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "validate", []))

    @builtins.property
    @jsii.member(jsii_name="backupPlanArn")
    def backup_plan_arn(self) -> builtins.str:
        '''The ARN of the backup plan.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "backupPlanArn"))

    @builtins.property
    @jsii.member(jsii_name="backupPlanId")
    def backup_plan_id(self) -> builtins.str:
        '''The identifier of the backup plan.'''
        return typing.cast(builtins.str, jsii.get(self, "backupPlanId"))

    @builtins.property
    @jsii.member(jsii_name="backupVault")
    def backup_vault(self) -> IBackupVault:
        '''The backup vault where backups are stored if not defined at the rule level.'''
        return typing.cast(IBackupVault, jsii.get(self, "backupVault"))

    @builtins.property
    @jsii.member(jsii_name="versionId")
    def version_id(self) -> builtins.str:
        '''Version Id.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "versionId"))


@jsii.implements(IBackupVault)
class BackupVault(
    _aws_cdk_core_f4b25747.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-backup.BackupVault",
):
    '''A backup vault.

    :exampleMetadata: infused

    Example::

        imported_vault = backup.BackupVault.from_backup_vault_name(self, "Vault", "myVaultName")
        
        role = iam.Role(self, "Access Role", assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"))
        
        imported_vault.grant(role, "backup:StartBackupJob")
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        access_policy: typing.Optional[_aws_cdk_aws_iam_940a1ce0.PolicyDocument] = None,
        backup_vault_name: typing.Optional[builtins.str] = None,
        block_recovery_point_deletion: typing.Optional[builtins.bool] = None,
        encryption_key: typing.Optional[_aws_cdk_aws_kms_e491a92b.IKey] = None,
        notification_events: typing.Optional[typing.Sequence[BackupVaultEvents]] = None,
        notification_topic: typing.Optional[_aws_cdk_aws_sns_889c7272.ITopic] = None,
        removal_policy: typing.Optional[_aws_cdk_core_f4b25747.RemovalPolicy] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param access_policy: A resource-based policy that is used to manage access permissions on the backup vault. Default: - access is not restricted
        :param backup_vault_name: The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the AWS Region where they are created. Default: - A CDK generated name
        :param block_recovery_point_deletion: Whether to add statements to the vault access policy that prevents anyone from deleting a recovery point. Default: false
        :param encryption_key: The server-side encryption key to use to protect your backups. Default: - an Amazon managed KMS key
        :param notification_events: The vault events to send. Default: - all vault events if ``notificationTopic`` is defined
        :param notification_topic: A SNS topic to send vault events to. Default: - no notifications
        :param removal_policy: The removal policy to apply to the vault. Note that removing a vault that contains recovery points will fail. Default: RemovalPolicy.RETAIN
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__164c2fb3e23cdf8e930a569486e656abe138fb2d2dffeb0386e47e875d1c6bdd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = BackupVaultProps(
            access_policy=access_policy,
            backup_vault_name=backup_vault_name,
            block_recovery_point_deletion=block_recovery_point_deletion,
            encryption_key=encryption_key,
            notification_events=notification_events,
            notification_topic=notification_topic,
            removal_policy=removal_policy,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromBackupVaultArn")
    @builtins.classmethod
    def from_backup_vault_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        backup_vault_arn: builtins.str,
    ) -> IBackupVault:
        '''Import an existing backup vault by arn.

        :param scope: -
        :param id: -
        :param backup_vault_arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ced55c8ddea9bc42d47011f8f6924d0fb89f30876bb9efade645d54501a0196)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument backup_vault_arn", value=backup_vault_arn, expected_type=type_hints["backup_vault_arn"])
        return typing.cast(IBackupVault, jsii.sinvoke(cls, "fromBackupVaultArn", [scope, id, backup_vault_arn]))

    @jsii.member(jsii_name="fromBackupVaultName")
    @builtins.classmethod
    def from_backup_vault_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        backup_vault_name: builtins.str,
    ) -> IBackupVault:
        '''Import an existing backup vault by name.

        :param scope: -
        :param id: -
        :param backup_vault_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b9326ad846ce6d4fafc5abb3b9c77526750e4f36249124ac1ce408b37fe276b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument backup_vault_name", value=backup_vault_name, expected_type=type_hints["backup_vault_name"])
        return typing.cast(IBackupVault, jsii.sinvoke(cls, "fromBackupVaultName", [scope, id, backup_vault_name]))

    @jsii.member(jsii_name="addToAccessPolicy")
    def add_to_access_policy(
        self,
        statement: _aws_cdk_aws_iam_940a1ce0.PolicyStatement,
    ) -> None:
        '''Adds a statement to the vault access policy.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12e4e3363a888db194774d7bc5d115348378e87371a58406cd81cc5559abe43a)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(None, jsii.invoke(self, "addToAccessPolicy", [statement]))

    @jsii.member(jsii_name="blockRecoveryPointDeletion")
    def block_recovery_point_deletion(self) -> None:
        '''Adds a statement to the vault access policy that prevents anyone from deleting a recovery point.'''
        return typing.cast(None, jsii.invoke(self, "blockRecoveryPointDeletion", []))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _aws_cdk_aws_iam_940a1ce0.IGrantable,
        *actions: builtins.str,
    ) -> _aws_cdk_aws_iam_940a1ce0.Grant:
        '''Grant the actions defined in actions to the given grantee on this Backup Vault resource.

        :param grantee: Principal to grant right to.
        :param actions: The actions to grant.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e86eee1a7d064db8d2d48176a947ce6a4bb7cdc9b4839f371efe09047c19403)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_aws_cdk_aws_iam_940a1ce0.Grant, jsii.invoke(self, "grant", [grantee, *actions]))

    @builtins.property
    @jsii.member(jsii_name="backupVaultArn")
    def backup_vault_arn(self) -> builtins.str:
        '''The ARN of the backup vault.'''
        return typing.cast(builtins.str, jsii.get(self, "backupVaultArn"))

    @builtins.property
    @jsii.member(jsii_name="backupVaultName")
    def backup_vault_name(self) -> builtins.str:
        '''The name of a logical container where backups are stored.'''
        return typing.cast(builtins.str, jsii.get(self, "backupVaultName"))


__all__ = [
    "BackupPlan",
    "BackupPlanProps",
    "BackupPlanRule",
    "BackupPlanRuleProps",
    "BackupResource",
    "BackupSelection",
    "BackupSelectionOptions",
    "BackupSelectionProps",
    "BackupVault",
    "BackupVaultEvents",
    "BackupVaultProps",
    "CfnBackupPlan",
    "CfnBackupPlanProps",
    "CfnBackupSelection",
    "CfnBackupSelectionProps",
    "CfnBackupVault",
    "CfnBackupVaultProps",
    "CfnFramework",
    "CfnFrameworkProps",
    "CfnReportPlan",
    "CfnReportPlanProps",
    "IBackupPlan",
    "IBackupVault",
    "TagCondition",
    "TagOperation",
]

publication.publish()

def _typecheckingstub__2acb2eb5bc1d067554bdcdfd30b36e01da252db9b56958ab5733e505368517ee(
    *,
    backup_plan_name: typing.Optional[builtins.str] = None,
    backup_plan_rules: typing.Optional[typing.Sequence[BackupPlanRule]] = None,
    backup_vault: typing.Optional[IBackupVault] = None,
    windows_vss: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f110a430335c0a2cadc6c66c132b0ea5d3fe0627f04ad81b4654afc1373b8e5(
    backup_vault: typing.Optional[IBackupVault] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c15208867c69a473d2e6a7c205c515634fd975057410c281b40435913774f65(
    backup_vault: typing.Optional[IBackupVault] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f38dbcdb3654b77cf7b041c4d0e1dd9372bca7757d2dc0b562932abcbdfde510(
    backup_vault: typing.Optional[IBackupVault] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52b6de1b57ab1725c4b3debdf9f46c0022dcc6bc0fb70e9dc5d6c7d6a3e9bd5d(
    backup_vault: typing.Optional[IBackupVault] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89d9135477decffd88cfe7297a0c68b34a8c1dc82c2de311099b66aa31c8c870(
    backup_vault: typing.Optional[IBackupVault] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89d1d01ed5709cfaad4c388e5791c6f275749bc559482d6625a5b9f232b804e2(
    *,
    backup_vault: typing.Optional[IBackupVault] = None,
    completion_window: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    delete_after: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    enable_continuous_backup: typing.Optional[builtins.bool] = None,
    move_to_cold_storage_after: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    rule_name: typing.Optional[builtins.str] = None,
    schedule_expression: typing.Optional[_aws_cdk_aws_events_efcdfa54.Schedule] = None,
    start_window: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9511c787f66a3b400ce49c7e9ace7abf3b5bdaf73c953eb33459c1a46da83c7e(
    resource: typing.Optional[builtins.str] = None,
    tag_condition: typing.Optional[typing.Union[TagCondition, typing.Dict[builtins.str, typing.Any]]] = None,
    construct: typing.Optional[_constructs_77d1e7e8.Construct] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdc90484c5f31d5acb6c903fe40f5017bff83ca657b2f8ad6a45d525c864b32b(
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d5274e11558a710a6465c4efc73c5940461b76f7c38973085611d292e66e265(
    construct: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efe968d8d893061c9b2e4ae72464c31535d419b940944207c36f78b5db9221ed(
    table: _aws_cdk_aws_dynamodb_eb1dc53b.ITable,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__438c3d8ec4e566e8bfd10a9463a8c497ae9a57884808b114410593e9677923bb(
    instance: _aws_cdk_aws_ec2_67de8e8d.IInstance,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c082fb5a6093279f9e88aade9235e065c2088f8417f2bc12a0dca57fd72366ff(
    file_system: _aws_cdk_aws_efs_b9f7a603.IFileSystem,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a97d5f6f97ce4a5882ec214ed68c59fac955d7f55a5c8c4bb4c283d8e50b1cf(
    instance: _aws_cdk_aws_rds_9543e6d5.IDatabaseInstance,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c339f15ec1fce1f739dcb83a56674fa9490f08ad4709bb733a17d3490829a9d(
    key: builtins.str,
    value: builtins.str,
    operation: typing.Optional[TagOperation] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dea399d8b73419df7fd11794674ce6a592c2f288198d53ac7e19679fa349a7a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    backup_plan: IBackupPlan,
    resources: typing.Sequence[BackupResource],
    allow_restores: typing.Optional[builtins.bool] = None,
    backup_selection_name: typing.Optional[builtins.str] = None,
    role: typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b88c60fb1713ec923f2ac9c23d30eb8b6b44ff2a99fe03094647b5cdfba2a3b(
    *,
    resources: typing.Sequence[BackupResource],
    allow_restores: typing.Optional[builtins.bool] = None,
    backup_selection_name: typing.Optional[builtins.str] = None,
    role: typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e70b1c7baf6a9648962e10d5080a92d126a38007360f96266e015c655874b03(
    *,
    resources: typing.Sequence[BackupResource],
    allow_restores: typing.Optional[builtins.bool] = None,
    backup_selection_name: typing.Optional[builtins.str] = None,
    role: typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole] = None,
    backup_plan: IBackupPlan,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ac441c7052b5e06554cd46a9f3d909913e6d4bfd680be32296a58b3ededaf32(
    *,
    access_policy: typing.Optional[_aws_cdk_aws_iam_940a1ce0.PolicyDocument] = None,
    backup_vault_name: typing.Optional[builtins.str] = None,
    block_recovery_point_deletion: typing.Optional[builtins.bool] = None,
    encryption_key: typing.Optional[_aws_cdk_aws_kms_e491a92b.IKey] = None,
    notification_events: typing.Optional[typing.Sequence[BackupVaultEvents]] = None,
    notification_topic: typing.Optional[_aws_cdk_aws_sns_889c7272.ITopic] = None,
    removal_policy: typing.Optional[_aws_cdk_core_f4b25747.RemovalPolicy] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b22513aceab736628f16f83e016a1e02a13f944c473f991529098b89737d72a(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    backup_plan: typing.Union[typing.Union[CfnBackupPlan.BackupPlanResourceTypeProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable],
    backup_plan_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a79e7ff0cfd5897d3704cab22d1908eb137f61444e7af9ce43223e52022b9352(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11e6584ce5574bd36e64401d7b12be835d7a54af655365835553a75450196a69(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dac3f789c2cd24168a7fbf45b8121e0024e194d459e2d5b9774c34764fceedf(
    value: typing.Union[CfnBackupPlan.BackupPlanResourceTypeProperty, _aws_cdk_core_f4b25747.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b032275b97a5a5e761ea70ab9ff73690e62462e878adf18a5fab7ddf0369feb1(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37f7df21270f46f72d0ffb25481fcf96303c4aec101812a683ecce4365d17acd(
    *,
    backup_options: typing.Any,
    resource_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5f7cc39f3ac3b75a6c9fd58cfc58413995b84b26a74781a055d8edc4f49d13a(
    *,
    backup_plan_name: builtins.str,
    backup_plan_rule: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[typing.Union[CfnBackupPlan.BackupRuleResourceTypeProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]]],
    advanced_backup_settings: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnBackupPlan.AdvancedBackupSettingResourceTypeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b287ba37827873fa303fa78a2cb621bcccc06adad7b5caa70bb3dceb6166e106(
    *,
    rule_name: builtins.str,
    target_backup_vault: builtins.str,
    completion_window_minutes: typing.Optional[jsii.Number] = None,
    copy_actions: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnBackupPlan.CopyActionResourceTypeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    enable_continuous_backup: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    lifecycle: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnBackupPlan.LifecycleResourceTypeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    recovery_point_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
    schedule_expression: typing.Optional[builtins.str] = None,
    start_window_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c8d9238e6c9aad30f4707d2a0bb5dfb22ffa1f941fbb53b8ffcaf42896f3f27(
    *,
    destination_backup_vault_arn: builtins.str,
    lifecycle: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnBackupPlan.LifecycleResourceTypeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f95ac72cdea9b5f2d90003a177be25c89cc7cc2e9a5afc0bdd407cd6a15cbf99(
    *,
    delete_after_days: typing.Optional[jsii.Number] = None,
    move_to_cold_storage_after_days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78bebf496bb7fbd732b6e916ccfc48ca7f82bb04b0fc30275559a53a691d2769(
    *,
    backup_plan: typing.Union[typing.Union[CfnBackupPlan.BackupPlanResourceTypeProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable],
    backup_plan_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e45952eebe3d558f21ca31af5c94fba3340cb712051449ea00c8ecebd2690a11(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    backup_plan_id: builtins.str,
    backup_selection: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnBackupSelection.BackupSelectionResourceTypeProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bc2b1b4f654afa86e6ab48546b87357ad30a0b35aa88c97fa84f932cc03783e(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__096ef63dbdd8e69e98ad67a1acc65b7d9a2a5eb1811e7d915bfe826d2a7283e3(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2470d1708af93b8366f2aab218f52ba5c3bcf56d840f7d8bb710510b9aa4fb6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79263fc95edbfd1311eb36845cdf5b605e282bab33688784c01d97c115e64ad4(
    value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnBackupSelection.BackupSelectionResourceTypeProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d62b37b6875ddb2c3923b17f42428c53878f71189ebf25d62ad6bd13c671b0d(
    *,
    iam_role_arn: builtins.str,
    selection_name: builtins.str,
    conditions: typing.Any = None,
    list_of_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnBackupSelection.ConditionResourceTypeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    not_resources: typing.Optional[typing.Sequence[builtins.str]] = None,
    resources: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ec2e118c097ddebac2dc76684f7ba1089b042c2c95d9df88739a851ed302d1b(
    *,
    condition_key: typing.Optional[builtins.str] = None,
    condition_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__230351d0c592b9ae2495166fc873edea23b9c56fcd59196f005253a3797b8a78(
    *,
    condition_key: builtins.str,
    condition_type: builtins.str,
    condition_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11ea9a50ad5cd9c04f7c48fcd3af05da80d6c0c32872d98a35450fe492127617(
    *,
    string_equals: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnBackupSelection.ConditionParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    string_like: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnBackupSelection.ConditionParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    string_not_equals: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnBackupSelection.ConditionParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    string_not_like: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnBackupSelection.ConditionParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a930a5cebaac7ba7f173bb848cfc290d9d01bd4205bf5f3650ceb467d3d7a07(
    *,
    backup_plan_id: builtins.str,
    backup_selection: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnBackupSelection.BackupSelectionResourceTypeProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7d0abd4b6c6f24669a1eaaab8bdefecbe7b5f458c5bfd19fc926cf6bed2adb5(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    backup_vault_name: builtins.str,
    access_policy: typing.Any = None,
    backup_vault_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
    encryption_key_arn: typing.Optional[builtins.str] = None,
    lock_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnBackupVault.LockConfigurationTypeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    notifications: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnBackupVault.NotificationObjectTypeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19a3d21b3f993f6310da73cd1b52794a2cf4ab173c1c1a7c10af4c986235fe67(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86fe929c5f0c15d7742bd88a6d8c20ed2d4a10bbd827dfe6156f6d5900f32393(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c71a77681867800b0b78f8f2964e810b8ca4726133d11f521526c72057717e9(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c56ff59ca47ea637fdabefb66a608321941d196bf6d2dceb2eea9346262e0f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__599d86302cbf47a25e092c9a19c1a8a79975cf921a6c65ac57925c27df6ae78f(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b7e5967a1c654d52c8f012c99b8973248dc38a07b13fd96c04780dc40269771(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b39c0ada04a33c8b6afdf71b70dc199ed3b70978eea3f5032cf3557509c9724a(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnBackupVault.LockConfigurationTypeProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db95d9f0c60d029a945ac4b6f7baa47e7ac2a37e13adf20171a0d39f8bdc96b4(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnBackupVault.NotificationObjectTypeProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63d1c1b3afe7f894e31f359203445ad304faf4b932ff3ed2e929aba3bde86b49(
    *,
    min_retention_days: jsii.Number,
    changeable_for_days: typing.Optional[jsii.Number] = None,
    max_retention_days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__114b4ccebf14c61a2b17165851e4fbe345051129158a340487a9f9a3f05da25b(
    *,
    backup_vault_events: typing.Sequence[builtins.str],
    sns_topic_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbdf05291db23d2caf60e2d70b4159d634f2bedc73d9fe37ee41bb25a24a9e55(
    *,
    backup_vault_name: builtins.str,
    access_policy: typing.Any = None,
    backup_vault_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
    encryption_key_arn: typing.Optional[builtins.str] = None,
    lock_configuration: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnBackupVault.LockConfigurationTypeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    notifications: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnBackupVault.NotificationObjectTypeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__825d958537f2a6be9e78e86f89e946b43c012fb159f6c7a60e3d1f6b6bb8ec45(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    framework_controls: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnFramework.FrameworkControlProperty, typing.Dict[builtins.str, typing.Any]]]]],
    framework_description: typing.Optional[builtins.str] = None,
    framework_name: typing.Optional[builtins.str] = None,
    framework_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1befd5d3aac330760979a0c05d9339d0d984bde78d506cd91e573904098799fc(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bb261cb62261a2673c1a1e2d56bb12fba1da8eb6abc14c639c6107ccd417747(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cdf2fe3743ee7a2f05c16cff11367c75b18107f549f681e41fd5dc1ba80129d(
    value: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, CfnFramework.FrameworkControlProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89059cc17b1b6f138564cec61ecca0b250b478032f26e17d8235ee857fac94ac(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fb5d8cf9105de9153d320b6efcdf6836b923b4584578b91320e76dcda44ba42(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__265d6dd1f31e75f3c4ab4c16495e04ebc3bc544dfeb405728cbcdb9fbd17f7db(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, _aws_cdk_core_f4b25747.CfnTag]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e52ff9df2b78b58a83f662858aa26b0b08dee7fc305aae8ae3fc316ba25e9f7a(
    *,
    parameter_name: builtins.str,
    parameter_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4531714524260b8596db2b33da6630acf20c71447f8603b1576569d02d364715(
    *,
    compliance_resource_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    compliance_resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03b0b19e58fb272ecebfc944079a5220ecd6c2620354a259e9f0c0ab8a16764b(
    *,
    control_name: builtins.str,
    control_input_parameters: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnFramework.ControlInputParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    control_scope: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cb80049cdda91bb4a7be90784452a3e2674eb27d1f8838437181c850788366a(
    *,
    framework_controls: typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnFramework.FrameworkControlProperty, typing.Dict[builtins.str, typing.Any]]]]],
    framework_description: typing.Optional[builtins.str] = None,
    framework_name: typing.Optional[builtins.str] = None,
    framework_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__390f524888340f40e5af7ec4fb30a9c65b2b2cae5e58e9e91929c1e6495ce2ba(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    report_delivery_channel: typing.Any,
    report_setting: typing.Any,
    report_plan_description: typing.Optional[builtins.str] = None,
    report_plan_name: typing.Optional[builtins.str] = None,
    report_plan_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db5f0d91e3c60eb327fd93d6aa938729558004a367ee968adbb55a74779c23c5(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03c8471b5d5b1ab9b4d92aea5dbc5d69ac7f68bd98877249f3852e8af3b81f78(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ce7706b39b2db939bbbb6cd7996caeeff8d947564992d1e2f7b6e169c37dbec(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a1f5e7e14384bfe189f6c12da3dc35e2f4a6e267f24aeeff8df66668e690eff(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13e056d728bb403ec0b42ee4744cf6e8bfdf32ae4defa39dfae3ca6070302f59(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__406b2829cb701e4dfd685f17f2579d51b232b4ab433cb05d8fed0e88955e78c4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__610ab7422f09eedcb67cf4dbda8dc7b5050833b36bd6b9245ee51aeddd623d5c(
    value: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, _aws_cdk_core_f4b25747.CfnTag]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89b9196515d065d7820b83d542ac81ae5ca3637423a638149f5deae68cd45055(
    *,
    s3_bucket_name: builtins.str,
    formats: typing.Optional[typing.Sequence[builtins.str]] = None,
    s3_key_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b391517c32a8e2a6ddf10ce1a41e6a1b3391208f50c3fabf1d50c89e80536082(
    *,
    report_template: builtins.str,
    accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
    framework_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    organization_units: typing.Optional[typing.Sequence[builtins.str]] = None,
    regions: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2efd0635581bb86b9b16facdfa93569f20269948d1e14439d8354cf9522a99c0(
    *,
    report_delivery_channel: typing.Any,
    report_setting: typing.Any,
    report_plan_description: typing.Optional[builtins.str] = None,
    report_plan_name: typing.Optional[builtins.str] = None,
    report_plan_tags: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9be7cb9a72282277bdb1999318759995687e0261947e074734bf3563ee32879c(
    grantee: _aws_cdk_aws_iam_940a1ce0.IGrantable,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b4d78dc0770c848384558d42a4d12762945fd9e1e21688cea4aed7750c53bef(
    *,
    key: builtins.str,
    value: builtins.str,
    operation: typing.Optional[TagOperation] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3996e8ae85f0f31ff5212254e44d9f3a1483fbc4a57606abacb1ac2648649b22(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    backup_plan_name: typing.Optional[builtins.str] = None,
    backup_plan_rules: typing.Optional[typing.Sequence[BackupPlanRule]] = None,
    backup_vault: typing.Optional[IBackupVault] = None,
    windows_vss: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f1f682073df85df9c67b8b68240013c0e22667c386b2c473c7c560dcb4061c2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    backup_vault: typing.Optional[IBackupVault] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a593977513729bb7363f767a1233ed191bdcc5af5075ac929e0cd79b03da51d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    backup_vault: typing.Optional[IBackupVault] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dbf7bbf30071fe58d8579890c51492755b2c0caacd1df612911764d3b833666(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    backup_vault: typing.Optional[IBackupVault] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd9e5ee6394bf689b4d9aefda6d363bb8b2685dd53fdd5cb1586cd316800eee2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    backup_vault: typing.Optional[IBackupVault] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d413ea15c25639b7e5ee6e75637b32483799be62ab2f38a1f00725dec454b4a2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    backup_plan_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beadee2174d8e3589491028eb012ae8cda0cee5f1139a97fed65ba6ba0a808a1(
    rule: BackupPlanRule,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d3bb42ef17a6534442b682780cc29b28c9cdbe725c5cd104654e2b214646cee(
    id: builtins.str,
    *,
    resources: typing.Sequence[BackupResource],
    allow_restores: typing.Optional[builtins.bool] = None,
    backup_selection_name: typing.Optional[builtins.str] = None,
    role: typing.Optional[_aws_cdk_aws_iam_940a1ce0.IRole] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__164c2fb3e23cdf8e930a569486e656abe138fb2d2dffeb0386e47e875d1c6bdd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    access_policy: typing.Optional[_aws_cdk_aws_iam_940a1ce0.PolicyDocument] = None,
    backup_vault_name: typing.Optional[builtins.str] = None,
    block_recovery_point_deletion: typing.Optional[builtins.bool] = None,
    encryption_key: typing.Optional[_aws_cdk_aws_kms_e491a92b.IKey] = None,
    notification_events: typing.Optional[typing.Sequence[BackupVaultEvents]] = None,
    notification_topic: typing.Optional[_aws_cdk_aws_sns_889c7272.ITopic] = None,
    removal_policy: typing.Optional[_aws_cdk_core_f4b25747.RemovalPolicy] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ced55c8ddea9bc42d47011f8f6924d0fb89f30876bb9efade645d54501a0196(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    backup_vault_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b9326ad846ce6d4fafc5abb3b9c77526750e4f36249124ac1ce408b37fe276b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    backup_vault_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12e4e3363a888db194774d7bc5d115348378e87371a58406cd81cc5559abe43a(
    statement: _aws_cdk_aws_iam_940a1ce0.PolicyStatement,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e86eee1a7d064db8d2d48176a947ce6a4bb7cdc9b4839f371efe09047c19403(
    grantee: _aws_cdk_aws_iam_940a1ce0.IGrantable,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
