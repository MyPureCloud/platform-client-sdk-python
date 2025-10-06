# ViewFilter

## ViewFilter

## Properties

|Name | Type | Description | Notes|
|------------ | ------------- | ------------- | -------------|
| **media_types** | list[str] | The media types are used to filter the view | [optional] |
| **queue_ids** | list[str] | The queue ids are used to filter the view | [optional] |
| **skill_ids** | list[str] | The skill ids are used to filter the view | [optional] |
| **assigned_skill_ids** | list[str] | The assigned user skill ids are used to filter the view | [optional] |
| **skill_groups** | list[str] | The skill groups used to filter the view | [optional] |
| **language_ids** | list[str] | The language ids are used to filter the view | [optional] |
| **assigned_language_ids** | list[str] | The assigned user language ids are used to filter the view | [optional] |
| **language_groups** | list[str] | The language groups used to filter the view | [optional] |
| **directions** | list[str] | The directions are used to filter the view | [optional] |
| **originating_directions** | list[str] | The list of orginating directions used to filter the view | [optional] |
| **wrap_up_codes** | list[str] | The wrap up codes are used to filter the view | [optional] |
| **dnis_list** | list[str] | The dnis list is used to filter the view | [optional] |
| **session_dnis_list** | list[str] | The list of session dnis used to filter the view | [optional] |
| **filter_queues_by_user_ids** | list[str] | The user ids are used to fetch associated queues for the view | [optional] |
| **filter_users_by_queue_ids** | list[str] | The queue ids are used to fetch associated users for the view | [optional] |
| **user_ids** | list[str] | The user ids are used to filter the view | [optional] |
| **management_unit_ids** | list[str] | The management unit ids are used to filter the view | [optional] |
| **address_tos** | list[str] | The address To values are used to filter the view | [optional] |
| **address_froms** | list[str] | The address from values are used to filter the view | [optional] |
| **outbound_campaign_ids** | list[str] | The outbound campaign ids are used to filter the view | [optional] |
| **outbound_contact_list_ids** | list[str] | The outbound contact list ids are used to filter the view | [optional] |
| **contact_ids** | list[str] | The contact ids are used to filter the view | [optional] |
| **external_contact_ids** | list[str] | The external contact ids are used to filter the view | [optional] |
| **external_org_ids** | list[str] | The external org ids are used to filter the view | [optional] |
| **ani_list** | list[str] | The ani list ids are used to filter the view | [optional] |
| **durations_milliseconds** | [list[NumericRange]](NumericRange) | The durations in milliseconds used to filter the view | [optional] |
| **acd_durations_milliseconds** | [list[NumericRange]](NumericRange) | The acd durations in milliseconds used to filter the view | [optional] |
| **talk_durations_milliseconds** | [list[NumericRange]](NumericRange) | The talk durations in milliseconds used to filter the view | [optional] |
| **acw_durations_milliseconds** | [list[NumericRange]](NumericRange) | The acw durations in milliseconds used to filter the view | [optional] |
| **handle_durations_milliseconds** | [list[NumericRange]](NumericRange) | The handle durations in milliseconds used to filter the view | [optional] |
| **hold_durations_milliseconds** | [list[NumericRange]](NumericRange) | The hold durations in milliseconds used to filter the view | [optional] |
| **abandon_durations_milliseconds** | [list[NumericRange]](NumericRange) | The abandon durations in milliseconds used to filter the view | [optional] |
| **evaluation_score** | [NumericRange](NumericRange) | The evaluationScore is used to filter the view | [optional] |
| **evaluation_critical_score** | [NumericRange](NumericRange) | The evaluationCriticalScore is used to filter the view | [optional] |
| **evaluation_form_ids** | list[str] | The evaluation form ids are used to filter the view | [optional] |
| **evaluated_agent_ids** | list[str] | The evaluated agent ids are used to filter the view | [optional] |
| **evaluator_ids** | list[str] | The evaluator ids are used to filter the view | [optional] |
| **transferred** | bool | Indicates filtering for transfers | [optional] |
| **abandoned** | bool | Indicates filtering for abandons | [optional] |
| **answered** | bool | Indicates filtering for answered interactions | [optional] |
| **message_types** | list[str] | The message media types used to filter the view | [optional] |
| **division_ids** | list[str] | The divison Ids used to filter the view | [optional] |
| **survey_form_ids** | list[str] | The survey form ids used to filter the view | [optional] |
| **survey_total_score** | [NumericRange](NumericRange) | The survey total score used to filter the view | [optional] |
| **survey_nps_score** | [NumericRange](NumericRange) | The survey NPS score used to filter the view | [optional] |
| **mos** | [NumericRange](NumericRange) | The desired range for mos values | [optional] |
| **survey_question_group_score** | [NumericRange](NumericRange) | The survey question group score used to filter the view | [optional] |
| **survey_promoter_score** | [NumericRange](NumericRange) | The survey promoter score used to filter the view | [optional] |
| **survey_form_context_ids** | list[str] | The list of survey form context ids used to filter the view | [optional] |
| **conversation_ids** | list[str] | The list of conversation ids used to filter the view | [optional] |
| **sip_call_ids** | list[str] | The list of SIP call ids used to filter the view | [optional] |
| **is_ended** | bool | Indicates filtering for ended | [optional] |
| **is_surveyed** | bool | Indicates filtering for survey | [optional] |
| **survey_scores** | [list[NumericRange]](NumericRange) | The list of survey score ranges used to filter the view | [optional] |
| **promoter_scores** | [list[NumericRange]](NumericRange) | The list of promoter score ranges used to filter the view | [optional] |
| **is_campaign** | bool | Indicates filtering for campaign | [optional] |
| **survey_statuses** | list[str] | The list of survey statuses used to filter the view | [optional] |
| **conversation_properties** | [ConversationProperties](ConversationProperties) | A grouping of conversation level filters | [optional] |
| **is_blind_transferred** | bool | Indicates filtering for blind transferred | [optional] |
| **is_consulted** | bool | Indicates filtering for consulted | [optional] |
| **is_consult_transferred** | bool | Indicates filtering for consult transferred | [optional] |
| **remote_participants** | list[str] | The list of remote participants used to filter the view | [optional] |
| **flow_ids** | list[str] | The list of flow Ids | [optional] |
| **flow_outcome_ids** | list[str] | A list of outcome ids of the flow | [optional] |
| **flow_outcome_values** | list[str] | A list of outcome values of the flow | [optional] |
| **flow_destination_types** | list[str] | The list of destination types of the flow | [optional] |
| **flow_disconnect_reasons** | list[str] | The list of reasons for the flow to disconnect | [optional] |
| **flow_types** | list[str] | A list of types of the flow | [optional] |
| **flow_entry_types** | list[str] | A list of types of the flow entry | [optional] |
| **flow_entry_reasons** | list[str] | A list of reasons of flow entry | [optional] |
| **flow_versions** | list[str] | A list of versions of a flow | [optional] |
| **group_ids** | list[str] | A list of directory group ids | [optional] |
| **has_journey_customer_id** | bool | Indicates filtering for journey customer id | [optional] |
| **has_journey_action_map_id** | bool | Indicates filtering for Journey action map id | [optional] |
| **has_journey_visit_id** | bool | Indicates filtering for Journey visit id | [optional] |
| **has_media** | bool | Indicates filtering for presence of MMS media | [optional] |
| **role_ids** | list[str] | The role Ids used to filter the view | [optional] |
| **reports_tos** | list[str] | The report to user IDs used to filter the view | [optional] |
| **location_ids** | list[str] | The location Ids used to filter the view | [optional] |
| **flow_out_types** | list[str] | A list of flow out types | [optional] |
| **provider_list** | list[str] | A list of providers | [optional] |
| **callback_number_list** | list[str] | A list of callback numbers or substrings of numbers (ex: [\&quot;317\&quot;, \&quot;13172222222\&quot;]) | [optional] |
| **callback_interval** | str | An interval of time to filter for scheduled callbacks. Intervals are represented as an ISO-8601 string. For example: YYYY-MM-DDThh:mm:ss/YYYY-MM-DDThh:mm:ss | [optional] |
| **used_routing_types** | list[str] | A list of routing types used | [optional] |
| **requested_routing_types** | list[str] | A list of routing types requested | [optional] |
| **has_agent_assist_id** | bool | Indicates filtering for agent assist id | [optional] |
| **transcripts** | [list[Transcripts]](Transcripts) | A list of transcript contents requested | [optional] |
| **transcript_languages** | list[str] | A list of transcript languages requested | [optional] |
| **participant_purposes** | list[str] | A list of participant purpose requested | [optional] |
| **show_first_queue** | bool | Indicates filtering for first queue data | [optional] |
| **team_ids** | list[str] | The team ids used to filter the view data | [optional] |
| **filter_users_by_team_ids** | list[str] | The team ids are used to fetch associated users for the view | [optional] |
| **journey_action_map_ids** | list[str] | The journey action map ids are used to fetch action maps for the associated view | [optional] |
| **journey_outcome_ids** | list[str] | The journey outcome ids are used to fetch outcomes for the associated view | [optional] |
| **journey_segment_ids** | list[str] | The journey segment ids are used to fetch segments for the associated view | [optional] |
| **journey_action_map_types** | list[str] | The journey action map types are used to filter action map data for the associated view | [optional] |
| **development_role_list** | list[str] | The list of development roles used to filter agent development view | [optional] |
| **development_type_list** | list[str] | The list of development types used to filter agent development view | [optional] |
| **development_status_list** | list[str] | The list of development status used to filter agent development view | [optional] |
| **development_module_ids** | list[str] | The list of development moduleIds used to filter agent development view | [optional] |
| **development_activity_overdue** | bool | Indicates filtering for development activities | [optional] |
| **customer_sentiment_score** | [NumericRange](NumericRange) | The customer sentiment score used to filter the view | [optional] |
| **customer_sentiment_trend** | [NumericRange](NumericRange) | The customer sentiment trend used to filter the view | [optional] |
| **flow_transfer_targets** | list[str] | The list of transfer targets used to filter flow data | [optional] |
| **development_name** | str | Filter for development name | [optional] |
| **topic_ids** | list[str] | Represents the topics detected in the transcript | [optional] |
| **external_tags** | list[str] | The list of external Tags used to filter conversation data | [optional] |
| **is_not_responding** | bool | Indicates filtering for not responding users | [optional] |
| **is_authenticated** | bool | Indicates filtering for the authenticated chat | [optional] |
| **bot_ids** | list[str] | The list of bot IDs used to filter bot views | [optional] |
| **bot_versions** | list[str] | The list of bot versions used to filter bot views | [optional] |
| **bot_message_types** | list[str] | The list of bot message types used to filter bot views | [optional] |
| **bot_provider_list** | list[str] | The list of bot providers used to filter bot views | [optional] |
| **bot_product_list** | list[str] | The list of bot products used to filter bot views | [optional] |
| **bot_recognition_failure_reason_list** | list[str] | The list of bot recognition failure reasons used to filter bot views | [optional] |
| **bot_intent_list** | list[str] | The list of bot intents used to filter bot views | [optional] |
| **bot_final_intent_list** | list[str] | The list of bot final intents used to filter bot views | [optional] |
| **bot_slot_list** | list[str] | The list of bot slots used to filter bot views | [optional] |
| **bot_result_list** | list[str] | The list of bot results used to filter bot views | [optional] |
| **blocked_reasons** | list[str] | The list of blocked reason used to filter action map constraints views | [optional] |
| **is_recorded** | bool | Indicates filtering for recorded | [optional] |
| **has_evaluation** | bool | Indicates filtering for evaluation | [optional] |
| **has_scored_evaluation** | bool | Indicates filtering for scored evaluation | [optional] |
| **email_delivery_status_list** | list[str] | The list of email delivery statuses used to filter views | [optional] |
| **is_agent_owned_callback** | bool | Indicates filtering for agent owned callback interactions | [optional] |
| **agent_callback_owner_ids** | list[str] | The list of callback owners used to filter interactions | [optional] |
| **transcript_topics** | [list[TranscriptTopics]](TranscriptTopics) | The list of transcript topics requested in filter | [optional] |
| **journey_frequency_cap_reasons** | list[str] | The list of frequency cap reasons to filter offer constraints | [optional] |
| **journey_blocking_action_map_ids** | list[str] | The list of blocking action maps to filter offer constraints | [optional] |
| **journey_action_target_ids** | list[str] | The list of action targets to filter offer constraints | [optional] |
| **journey_blocking_schedule_group_ids** | list[str] | The list of blocking schedule groups to filter offer constraints | [optional] |
| **journey_blocking_emergency_schedule_group_ids** | list[str] | The list of emergency schedule groups to filter offer constraints | [optional] |
| **journey_url_equal_conditions** | list[str] | The list of url equal conditions to filter offer constraints | [optional] |
| **journey_url_not_equal_conditions** | list[str] | The list of url not equal conditions to filter offer constraints | [optional] |
| **journey_url_starts_with_conditions** | list[str] | The list of url starts with conditions to filter offer constraints | [optional] |
| **journey_url_ends_with_conditions** | list[str] | The list of url ends with conditions to filter offer constraints | [optional] |
| **journey_url_contains_any_conditions** | list[str] | The list of url contains any conditions to filter offer constraints | [optional] |
| **journey_url_not_contains_any_conditions** | list[str] | The list of url not contains any conditions to filter offer constraints | [optional] |
| **journey_url_contains_all_conditions** | list[str] | The list of url contains all conditions to filter offer constraints | [optional] |
| **journey_url_not_contains_all_conditions** | list[str] | The list of url not contains all conditions to filter offer constraints | [optional] |
| **flow_milestone_ids** | list[str] | The list of flow milestones to filter exports | [optional] |
| **is_assessment_passed** | bool | Filter to indicate if Agent passed assessment or not | [optional] |
| **conversation_initiators** | list[str] | The list to filter based on Brands (Bot/User/Agent) or End User who initiated the first message in the conversation | [optional] |
| **has_customer_participated** | bool | Indicates if the customer has participated in an initiated conversation | [optional] |
| **is_acd_interaction** | bool | Filter to indicate if interaction was ACD or non-ACD | [optional] |
| **has_fax** | bool | Filters to indicate if interaction has FAX | [optional] |
| **data_action_ids** | list[str] | The list of Data Action IDs  | [optional] |
| **action_category_name** | str | Deprecated - Please use integrationIds instead | [optional] |
| **integration_ids** | list[str] | The list of integration IDs for Data Action | [optional] |
| **response_statuses** | list[str] | The list of Response codes for Data Action | [optional] |
| **available_dashboard** | str | Filter to indicate the availability of the dashboard is public or private. | [optional] |
| **favourite_dashboard** | bool | Filter to indicate whether the dashboard is favorite or unfavorite. | [optional] |
| **my_dashboard** | bool | Filter to indicate the dashboard owned by the user. | [optional] |
| **station_errors** | list[str] | The list of agent errors that are related to station | [optional] |
| **canonical_contact_ids** | list[str] | The canonical contact ids are used to filter the view | [optional] |
| **alert_rule_ids** | list[str] | The list of Alert Rule IDs | [optional] |
| **evaluation_form_context_ids** | list[str] | The list of Evaluation Form Context IDs | [optional] |
| **evaluation_statuses** | list[str] | The evaluation statuses that are used to filter the view | [optional] |
| **workbin_ids** | list[str] | The list of Workbin IDs | [optional] |
| **worktype_ids** | list[str] | The list of Worktype IDs | [optional] |
| **workitem_ids** | list[str] | The list of Workitem IDs | [optional] |
| **workitem_assignee_ids** | list[str] | The list of Workitem Assignee IDs | [optional] |
| **workitem_statuses** | list[str] | The list of Workitem Statuses IDs | [optional] |
| **is_analyzed_for_sensitive_data** | bool | Deprecated - Use hasPciData or hasPiiData instead. | [optional] |
| **has_sensitive_data** | bool | Deprecated. Use hasPciData or hasPiiData instead. | [optional] |
| **has_pci_data** | bool | Filter to indicate the transcript contains Pci data. | [optional] |
| **has_pii_data** | bool | Filter to indicate the transcript contains Pii data. | [optional] |
| **sub_path** | str | Filter for Sub Path | [optional] |
| **user_state** | str | The user supplied state value in the view | [optional] |
| **is_cleared_by_customer** | bool | Filter to indicate if the customer cleared the conversation. | [optional] |
| **evaluation_assignee_ids** | list[str] | The evaluation assignee ids that are used to filter the view. | [optional] |
| **evaluation_assigned** | bool | Filter to indicate that the user has no assigned evaluation. | [optional] |
| **assistant_ids** | list[str] | The assistant ids that are used to filter the view. | [optional] |
| **knowledge_base_ids** | list[str] | The knowledge base ids that are used to filter the view. | [optional] |
| **is_parked** | bool | Filter to indicate if the interactions are parked. | [optional] |
| **agent_empathy_score** | [NumericRange](NumericRange) | The agentEmpathyScore is used to filter the view | [optional] |
| **survey_types** | list[str] | The surveyTypes is used to filter the view | [optional] |
| **survey_response_statuses** | list[str] | The list of Survey Response Status | [optional] |
| **bot_flow_types** | list[str] | The botFlowTypes is used to filter the view | [optional] |
| **agent_talk_duration_milliseconds** | [list[NumericRange]](NumericRange) | The agent talk durations in milliseconds used to filter the view | [optional] |
| **customer_talk_duration_milliseconds** | [list[NumericRange]](NumericRange) | The customer talk durations in milliseconds used to filter the view | [optional] |
| **overtalk_duration_milliseconds** | [list[NumericRange]](NumericRange) | The overtalk durations in milliseconds used to filter the view | [optional] |
| **silence_duration_milliseconds** | [list[NumericRange]](NumericRange) | The silence durations in milliseconds used to filter the view | [optional] |
| **acd_duration_milliseconds** | [list[NumericRange]](NumericRange) | The acd durations in milliseconds used to filter the view | [optional] |
| **ivr_duration_milliseconds** | [list[NumericRange]](NumericRange) | The ivr durations in milliseconds used to filter the view | [optional] |
| **other_duration_milliseconds** | [list[NumericRange]](NumericRange) | The other (hold/music) durations in milliseconds used to filter the view | [optional] |
| **agent_talk_percentage** | [NumericRange](NumericRange) | The agent talk percentage used to filter the view | [optional] |
| **customer_talk_percentage** | [NumericRange](NumericRange) | The customer talk percentage used to filter the view | [optional] |
| **overtalk_percentage** | [NumericRange](NumericRange) | The overtalk percentage used to filter the view | [optional] |
| **silence_percentage** | [NumericRange](NumericRange) | The silence percentage used to filter the view | [optional] |
| **acd_percentage** | [NumericRange](NumericRange) | The acd percentage used to filter the view | [optional] |
| **ivr_percentage** | [NumericRange](NumericRange) | The ivr percentage used to filter the view | [optional] |
| **other_percentage** | [NumericRange](NumericRange) | The other (hold/music percentage used to filter the view | [optional] |
| **overtalk_instances** | [NumericRange](NumericRange) | The overtalk instance range used to filter the view | [optional] |
| **is_screen_recorded** | bool | Filter to indicate if the screen is recorded | [optional] |
| **screen_monitor_user_ids** | list[str] | The list of Screen Monitor User Ids | [optional] |
| **dashboard_state** | str | The state of dashboard being filtered | [optional] |
| **dashboard_type** | str | The type of dashboard being filtered | [optional] |
| **dashboard_access_filter** | str | The type of dashboard access being filtered | [optional] |
| **transcript_duration_milliseconds** | [list[NumericRange]](NumericRange) | The transcript durations in milliseconds used to filter the view | [optional] |
| **workitems_statuses** | [list[WorkitemStatusFilter]](WorkitemStatusFilter) | The list of workitem status with worktype | [optional] |
| **social_countries** | list[str] | List of countries for social filtering | [optional] |
| **social_languages** | list[str] | List of languages for social filtering | [optional] |
| **social_channels** | list[str] | List of channels for social filtering | [optional] |
| **social_sentiment_category** | list[str] | The sentiment of the social post | [optional] |
| **social_topic_ids** | list[str] | The list of topicIds for social filtering | [optional] |
| **social_ingestion_rule_ids** | list[str] | The list of ingestion ruleIds for social filtering | [optional] |
| **social_conversation_created** | bool | Filter to indicate if the post has created a conversation | [optional] |
| **social_content_type** | list[str] | The list of content Type for social filtering | [optional] |
| **social_keywords** | [list[SocialKeyword]](SocialKeyword) | The list of keywords for social filtering | [optional] |
| **social_post_escalated** | bool | Filter to indicate if the post is escalated | [optional] |
| **social_classifications** | list[str] | Indicates if a social message was public or private | [optional] |
| **filter_users_by_manager_ids** | list[str] | The manager ids used to fetch associated users for the view | [optional] |
| **slideshow_ids** | list[str] | List of Dashboard slideshowIds to be filtered | [optional] |
| **conferenced** | bool | Filter to indicate if the conversation has conference | [optional] |
| **video** | bool | Filter to indicate if the conversation has video | [optional] |
| **linked_interaction** | bool | Filter to indicate if the conversation has linked interaction | [optional] |
| **recommendation_sources** | list[str] | List of recommendation sources for filtering recommendation details pane | [optional] |
| **evaluation_role** | str | Sets the role when viewing agent evaluations | [optional] |
| **comparison_queue_ids** | list[str] | The queue ids are used to for comparison to the primary queue filter in reporting | [optional] |
| **view_metrics** | list[str] | A list of metrics selected for the view | [optional] |
| **timeline_categories** | list[str] | A list of timeline categories | [optional] |
| **acw** | bool | Filter to indicate for acw state | [optional] |
| **segment_types** | list[str] | A list of filtered segment types | [optional] |
| **program_ids** | list[str] | A list of program ids for filtering | [optional] |
| **category_ids** | list[str] | A list of category ids for filtering | [optional] |
| **delivery_pushed** | bool | Filter to indicate if push notification is sent | [optional] |
| **social_ratings** | list[float] | A set of ratings for Google Business Profile | [optional] |
| **virtual_agent_ids** | list[str] | A list of virtual agent ids for filtering. | [optional] |
| **empathy_score_categories** | list[str] | A set of Empathy Score Categories for filtering | [optional] |
| **sentiment_score_categories** | list[str] | A set of Sentiment Score Categories  for filtering | [optional] |
| **sentiment_trend_categories** | list[str] | A set of Sentiment Trend Categories for filtering | [optional] |
| **content_moderation_flags** | list[str] | A set of Content Moderation Flags for filtering | [optional] |



_PureCloudPlatformClientV2 240.0.0_
