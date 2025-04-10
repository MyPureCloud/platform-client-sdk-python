# WorkforceManagementApi

## PureCloudPlatformClientV2.WorkforceManagementApi

All URIs are relative to *https://api.mypurecloud.com*

|Method | Description|
|------------- | -------------|
|[**delete_workforcemanagement_businessunit**](#delete_workforcemanagement_businessunit) | Delete business unit|
|[**delete_workforcemanagement_businessunit_activitycode**](#delete_workforcemanagement_businessunit_activitycode) | Deletes an activity code|
|[**delete_workforcemanagement_businessunit_planninggroup**](#delete_workforcemanagement_businessunit_planninggroup) | Deletes the planning group|
|[**delete_workforcemanagement_businessunit_scheduling_run**](#delete_workforcemanagement_businessunit_scheduling_run) | Cancel a scheduling run|
|[**delete_workforcemanagement_businessunit_servicegoaltemplate**](#delete_workforcemanagement_businessunit_servicegoaltemplate) | Delete a service goal template|
|[**delete_workforcemanagement_businessunit_staffinggroup**](#delete_workforcemanagement_businessunit_staffinggroup) | Deletes a staffing group|
|[**delete_workforcemanagement_businessunit_timeofflimit**](#delete_workforcemanagement_businessunit_timeofflimit) | Deletes a time-off limit object|
|[**delete_workforcemanagement_businessunit_timeoffplan**](#delete_workforcemanagement_businessunit_timeoffplan) | Deletes a time-off plan|
|[**delete_workforcemanagement_businessunit_week_schedule**](#delete_workforcemanagement_businessunit_week_schedule) | Delete a schedule|
|[**delete_workforcemanagement_businessunit_week_shorttermforecast**](#delete_workforcemanagement_businessunit_week_shorttermforecast) | Delete a short term forecast|
|[**delete_workforcemanagement_businessunit_workplanbid**](#delete_workforcemanagement_businessunit_workplanbid) | Delete a work plan bid|
|[**delete_workforcemanagement_businessunit_workplanbid_group**](#delete_workforcemanagement_businessunit_workplanbid_group) | Delete a bid group by bid group Id|
|[**delete_workforcemanagement_calendar_url_ics**](#delete_workforcemanagement_calendar_url_ics) | Disable generated calendar link for the current user|
|[**delete_workforcemanagement_managementunit**](#delete_workforcemanagement_managementunit) | Delete management unit|
|[**delete_workforcemanagement_managementunit_timeofflimit**](#delete_workforcemanagement_managementunit_timeofflimit) | Deletes a time off limit object|
|[**delete_workforcemanagement_managementunit_timeoffplan**](#delete_workforcemanagement_managementunit_timeoffplan) | Deletes a time off plan|
|[**delete_workforcemanagement_managementunit_workplan**](#delete_workforcemanagement_managementunit_workplan) | Delete a work plan|
|[**delete_workforcemanagement_managementunit_workplanrotation**](#delete_workforcemanagement_managementunit_workplanrotation) | Delete a work plan rotation|
|[**get_workforcemanagement_adherence**](#get_workforcemanagement_adherence) | Get a list of UserScheduleAdherence records for the requested users|
|[**get_workforcemanagement_adherence_explanation**](#get_workforcemanagement_adherence_explanation) | Get an adherence explanation for the current user|
|[**get_workforcemanagement_adherence_explanations_job**](#get_workforcemanagement_adherence_explanations_job) | Query the status of an adherence explanation operation. Only the user who started the operation can query the status|
|[**get_workforcemanagement_adherence_historical_bulk_job**](#get_workforcemanagement_adherence_historical_bulk_job) | Request to fetch the status of the historical adherence bulk job. Only the user who started the operation can query the status|
|[**get_workforcemanagement_adherence_historical_job**](#get_workforcemanagement_adherence_historical_job) | Query the status of a historical adherence request operation. Only the user who started the operation can query the status|
|[**get_workforcemanagement_agent_adherence_explanation**](#get_workforcemanagement_agent_adherence_explanation) | Get an adherence explanation|
|[**get_workforcemanagement_agent_managementunit**](#get_workforcemanagement_agent_managementunit) | Get the management unit to which the agent belongs|
|[**get_workforcemanagement_agents_me_managementunit**](#get_workforcemanagement_agents_me_managementunit) | Get the management unit to which the currently logged in agent belongs|
|[**get_workforcemanagement_alternativeshifts_offers_job**](#get_workforcemanagement_alternativeshifts_offers_job) | Query the status of an alternative shift offers operation. Only the user who started the operation can query the status|
|[**get_workforcemanagement_alternativeshifts_offers_search_job**](#get_workforcemanagement_alternativeshifts_offers_search_job) | Query the status of an alternative shift search offers operation. Only the user who started the operation can query the status|
|[**get_workforcemanagement_alternativeshifts_settings**](#get_workforcemanagement_alternativeshifts_settings) | Get alternative shifts settings from the current logged in agent’s business unit|
|[**get_workforcemanagement_alternativeshifts_trade**](#get_workforcemanagement_alternativeshifts_trade) | Get my alternative shift trade by trade ID|
|[**get_workforcemanagement_alternativeshifts_trades**](#get_workforcemanagement_alternativeshifts_trades) | Get a list of my alternative shifts trades|
|[**get_workforcemanagement_alternativeshifts_trades_job**](#get_workforcemanagement_alternativeshifts_trades_job) | Query the status of an alternative shift trades operation. Only the user who started the operation can query the status|
|[**get_workforcemanagement_alternativeshifts_trades_state_job**](#get_workforcemanagement_alternativeshifts_trades_state_job) | Query the status of an alternative shift trade state operation. Only the user who started the operation can query the status|
|[**get_workforcemanagement_businessunit**](#get_workforcemanagement_businessunit) | Get business unit|
|[**get_workforcemanagement_businessunit_activitycode**](#get_workforcemanagement_businessunit_activitycode) | Get an activity code|
|[**get_workforcemanagement_businessunit_activitycodes**](#get_workforcemanagement_businessunit_activitycodes) | Get activity codes|
|[**get_workforcemanagement_businessunit_activityplan**](#get_workforcemanagement_businessunit_activityplan) | Get an activity plan|
|[**get_workforcemanagement_businessunit_activityplan_runs_job**](#get_workforcemanagement_businessunit_activityplan_runs_job) | Gets an activity plan run job|
|[**get_workforcemanagement_businessunit_activityplans**](#get_workforcemanagement_businessunit_activityplans) | Get activity plans|
|[**get_workforcemanagement_businessunit_activityplans_jobs**](#get_workforcemanagement_businessunit_activityplans_jobs) | Gets the latest job for all activity plans in the business unit|
|[**get_workforcemanagement_businessunit_alternativeshifts_settings**](#get_workforcemanagement_businessunit_alternativeshifts_settings) | Get alternative shifts settings for a business unit|
|[**get_workforcemanagement_businessunit_alternativeshifts_trade**](#get_workforcemanagement_businessunit_alternativeshifts_trade) | Get an alternative shifts trade in a business unit for a given trade ID|
|[**get_workforcemanagement_businessunit_alternativeshifts_trades_search_job**](#get_workforcemanagement_businessunit_alternativeshifts_trades_search_job) | Query the status of an alternative shift search trade operation. Only the user who started the operation can query the status|
|[**get_workforcemanagement_businessunit_intraday_planninggroups**](#get_workforcemanagement_businessunit_intraday_planninggroups) | Get intraday planning groups for the given date|
|[**get_workforcemanagement_businessunit_mainforecast_continuousforecast_session**](#get_workforcemanagement_businessunit_mainforecast_continuousforecast_session) | Get the latest session for the business unit ID|
|[**get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id**](#get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id) | Get the session details for the session ID|
|[**get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id_snapshot_snapshot_id**](#get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id_snapshot_snapshot_id) | Get the snapshot details for the snapshot ID|
|[**get_workforcemanagement_businessunit_managementunits**](#get_workforcemanagement_businessunit_managementunits) | Get all authorized management units in the business unit|
|[**get_workforcemanagement_businessunit_planninggroup**](#get_workforcemanagement_businessunit_planninggroup) | Get a planning group|
|[**get_workforcemanagement_businessunit_planninggroups**](#get_workforcemanagement_businessunit_planninggroups) | Gets list of planning groups|
|[**get_workforcemanagement_businessunit_scheduling_run**](#get_workforcemanagement_businessunit_scheduling_run) | Get a scheduling run|
|[**get_workforcemanagement_businessunit_scheduling_run_result**](#get_workforcemanagement_businessunit_scheduling_run_result) | Get the result of a rescheduling operation|
|[**get_workforcemanagement_businessunit_scheduling_runs**](#get_workforcemanagement_businessunit_scheduling_runs) | Get the list of scheduling runs|
|[**get_workforcemanagement_businessunit_servicegoaltemplate**](#get_workforcemanagement_businessunit_servicegoaltemplate) | Get a service goal template|
|[**get_workforcemanagement_businessunit_servicegoaltemplates**](#get_workforcemanagement_businessunit_servicegoaltemplates) | Gets list of service goal templates|
|[**get_workforcemanagement_businessunit_staffinggroup**](#get_workforcemanagement_businessunit_staffinggroup) | Gets a staffing group|
|[**get_workforcemanagement_businessunit_staffinggroups**](#get_workforcemanagement_businessunit_staffinggroups) | Gets a list of staffing groups|
|[**get_workforcemanagement_businessunit_timeofflimit**](#get_workforcemanagement_businessunit_timeofflimit) | Gets a time-off limit object|
|[**get_workforcemanagement_businessunit_timeofflimits**](#get_workforcemanagement_businessunit_timeofflimits) | Gets a list of time-off limit objects|
|[**get_workforcemanagement_businessunit_timeoffplan**](#get_workforcemanagement_businessunit_timeoffplan) | Gets a time-off plan|
|[**get_workforcemanagement_businessunit_timeoffplans**](#get_workforcemanagement_businessunit_timeoffplans) | Gets a list of time-off plans|
|[**get_workforcemanagement_businessunit_week_schedule**](#get_workforcemanagement_businessunit_week_schedule) | Get the metadata for the schedule, describing which management units and agents are in the scheduleSchedule data can then be loaded with the query route|
|[**get_workforcemanagement_businessunit_week_schedule_generationresults**](#get_workforcemanagement_businessunit_week_schedule_generationresults) | Get the generation results for a generated schedule|
|[**get_workforcemanagement_businessunit_week_schedule_headcountforecast**](#get_workforcemanagement_businessunit_week_schedule_headcountforecast) | Get the headcount forecast by planning group for the schedule|
|[**get_workforcemanagement_businessunit_week_schedule_history_agent**](#get_workforcemanagement_businessunit_week_schedule_history_agent) | Loads agent&#39;s schedule history.|
|[**get_workforcemanagement_businessunit_week_schedule_performancepredictions**](#get_workforcemanagement_businessunit_week_schedule_performancepredictions) | Get the performance prediction for the associated schedule|
|[**get_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculation**](#get_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculation) | Get recalculated performance prediction result|
|[**get_workforcemanagement_businessunit_week_schedules**](#get_workforcemanagement_businessunit_week_schedules) | Get the list of week schedules for the specified week|
|[**get_workforcemanagement_businessunit_week_shorttermforecast**](#get_workforcemanagement_businessunit_week_shorttermforecast) | Get a short term forecast|
|[**get_workforcemanagement_businessunit_week_shorttermforecast_data**](#get_workforcemanagement_businessunit_week_shorttermforecast_data) | Get the result of a short term forecast calculation|
|[**get_workforcemanagement_businessunit_week_shorttermforecast_generationresults**](#get_workforcemanagement_businessunit_week_shorttermforecast_generationresults) | Gets the forecast generation results|
|[**get_workforcemanagement_businessunit_week_shorttermforecast_longtermforecastdata**](#get_workforcemanagement_businessunit_week_shorttermforecast_longtermforecastdata) | Get the result of a long term forecast calculation|
|[**get_workforcemanagement_businessunit_week_shorttermforecast_planninggroups**](#get_workforcemanagement_businessunit_week_shorttermforecast_planninggroups) | Gets the forecast planning group snapshot|
|[**get_workforcemanagement_businessunit_week_shorttermforecast_staffingrequirement**](#get_workforcemanagement_businessunit_week_shorttermforecast_staffingrequirement) | Get the staffing requirement by planning group for a forecast|
|[**get_workforcemanagement_businessunit_week_shorttermforecasts**](#get_workforcemanagement_businessunit_week_shorttermforecasts) | Get short term forecasts|
|[**get_workforcemanagement_businessunit_workplanbid**](#get_workforcemanagement_businessunit_workplanbid) | Get a work plan bid|
|[**get_workforcemanagement_businessunit_workplanbid_group**](#get_workforcemanagement_businessunit_workplanbid_group) | Get a bid group by bid group Id|
|[**get_workforcemanagement_businessunit_workplanbid_group_preferences**](#get_workforcemanagement_businessunit_workplanbid_group_preferences) | Gets the work plan preferences of all the agents in the work plan bid group|
|[**get_workforcemanagement_businessunit_workplanbid_groups_summary**](#get_workforcemanagement_businessunit_workplanbid_groups_summary) | Get summary of bid groups that belong to a work plan bid|
|[**get_workforcemanagement_businessunit_workplanbids**](#get_workforcemanagement_businessunit_workplanbids) | Get list of work plan bids|
|[**get_workforcemanagement_businessunits**](#get_workforcemanagement_businessunits) | Get business units|
|[**get_workforcemanagement_businessunits_divisionviews**](#get_workforcemanagement_businessunits_divisionviews) | Get business units across divisions|
|[**get_workforcemanagement_calendar_data_ics**](#get_workforcemanagement_calendar_data_ics) | Get ics formatted calendar based on shareable link|
|[**get_workforcemanagement_calendar_url_ics**](#get_workforcemanagement_calendar_url_ics) | Get existing calendar link for the current user|
|[**get_workforcemanagement_historicaldata_bulk_remove_job**](#get_workforcemanagement_historicaldata_bulk_remove_job) | Retrieves delete job status for historical data imports associated with the job id|
|[**get_workforcemanagement_historicaldata_bulk_remove_jobs**](#get_workforcemanagement_historicaldata_bulk_remove_jobs) | Retrieves all delete job status for historical data|
|[**get_workforcemanagement_historicaldata_deletejob**](#get_workforcemanagement_historicaldata_deletejob) | Retrieves delete job status for historical data imports of the organization.|
|[**get_workforcemanagement_historicaldata_importstatus**](#get_workforcemanagement_historicaldata_importstatus) | Retrieves status of the historical data imports of the organization|
|[**get_workforcemanagement_historicaldata_importstatus_job_id**](#get_workforcemanagement_historicaldata_importstatus_job_id) | Retrieves status of the historical data imports associated with job id|
|[**get_workforcemanagement_integrations_hris**](#get_workforcemanagement_integrations_hris) | Get integrations|
|[**get_workforcemanagement_integrations_hris_timeofftypes_job**](#get_workforcemanagement_integrations_hris_timeofftypes_job) | Query the results of time off types job|
|[**get_workforcemanagement_managementunit**](#get_workforcemanagement_managementunit) | Get management unit|
|[**get_workforcemanagement_managementunit_activitycodes**](#get_workforcemanagement_managementunit_activitycodes) | Deprecated: Instead use /api/v2/workforcemanagement/businessunits/{businessUnitId}/activitycodes. Get the list of activity codes|
|[**get_workforcemanagement_managementunit_adherence**](#get_workforcemanagement_managementunit_adherence) | Get a list of user schedule adherence records for the requested management unit|
|[**get_workforcemanagement_managementunit_agent**](#get_workforcemanagement_managementunit_agent) | Get data for agent in the management unit|
|[**get_workforcemanagement_managementunit_agent_shifttrades**](#get_workforcemanagement_managementunit_agent_shifttrades) | Gets all the shift trades for a given agent|
|[**get_workforcemanagement_managementunit_shifttrades_matched**](#get_workforcemanagement_managementunit_shifttrades_matched) | Gets a summary of all shift trades in the matched state|
|[**get_workforcemanagement_managementunit_shifttrades_users**](#get_workforcemanagement_managementunit_shifttrades_users) | Gets list of users available for whom you can send direct shift trade requests|
|[**get_workforcemanagement_managementunit_timeofflimit**](#get_workforcemanagement_managementunit_timeofflimit) | Gets a time off limit object|
|[**get_workforcemanagement_managementunit_timeofflimits**](#get_workforcemanagement_managementunit_timeofflimits) | Gets a list of time off limit objects under management unit.|
|[**get_workforcemanagement_managementunit_timeoffplan**](#get_workforcemanagement_managementunit_timeoffplan) | Gets a time off plan|
|[**get_workforcemanagement_managementunit_timeoffplans**](#get_workforcemanagement_managementunit_timeoffplans) | Gets a list of time off plans|
|[**get_workforcemanagement_managementunit_user_timeoffrequest**](#get_workforcemanagement_managementunit_user_timeoffrequest) | Get a time off request|
|[**get_workforcemanagement_managementunit_user_timeoffrequest_timeofflimits**](#get_workforcemanagement_managementunit_user_timeoffrequest_timeofflimits) | Retrieves time off limit, allocated and waitlisted values according to specific time off request|
|[**get_workforcemanagement_managementunit_user_timeoffrequests**](#get_workforcemanagement_managementunit_user_timeoffrequests) | Get a list of time off requests for a given user|
|[**get_workforcemanagement_managementunit_users**](#get_workforcemanagement_managementunit_users) | Get users in the management unit|
|[**get_workforcemanagement_managementunit_week_schedule**](#get_workforcemanagement_managementunit_week_schedule) | Deprecated.  Use the equivalent business unit resource instead. Get a week schedule|
|[**get_workforcemanagement_managementunit_week_schedules**](#get_workforcemanagement_managementunit_week_schedules) | Deprecated.  Use the equivalent business unit resource instead. Get the list of schedules in a week in management unit|
|[**get_workforcemanagement_managementunit_week_shifttrades**](#get_workforcemanagement_managementunit_week_shifttrades) | Gets all the shift trades for a given week|
|[**get_workforcemanagement_managementunit_workplan**](#get_workforcemanagement_managementunit_workplan) | Get a work plan|
|[**get_workforcemanagement_managementunit_workplanrotation**](#get_workforcemanagement_managementunit_workplanrotation) | Get a work plan rotation|
|[**get_workforcemanagement_managementunit_workplanrotations**](#get_workforcemanagement_managementunit_workplanrotations) | Get work plan rotations|
|[**get_workforcemanagement_managementunit_workplans**](#get_workforcemanagement_managementunit_workplans) | Get work plans|
|[**get_workforcemanagement_managementunits**](#get_workforcemanagement_managementunits) | Get management units|
|[**get_workforcemanagement_managementunits_divisionviews**](#get_workforcemanagement_managementunits_divisionviews) | Get management units across divisions|
|[**get_workforcemanagement_notifications**](#get_workforcemanagement_notifications) | Get a list of notifications for the current user|
|[**get_workforcemanagement_schedulingjob**](#get_workforcemanagement_schedulingjob) | Get status of the scheduling job|
|[**get_workforcemanagement_shifttrades**](#get_workforcemanagement_shifttrades) | Gets all of my shift trades|
|[**get_workforcemanagement_shrinkage_job**](#get_workforcemanagement_shrinkage_job) | Request to fetch the status of the historical shrinkage query|
|[**get_workforcemanagement_timeoffbalance_job**](#get_workforcemanagement_timeoffbalance_job) | Query the results of time off types job|
|[**get_workforcemanagement_timeoffrequest**](#get_workforcemanagement_timeoffrequest) | Get a time off request for the current user|
|[**get_workforcemanagement_timeoffrequest_waitlistpositions**](#get_workforcemanagement_timeoffrequest_waitlistpositions) | Get the daily waitlist positions of a time off request for the current user|
|[**get_workforcemanagement_timeoffrequests**](#get_workforcemanagement_timeoffrequests) | Get a list of time off requests for the current user|
|[**get_workforcemanagement_user_workplanbidranks**](#get_workforcemanagement_user_workplanbidranks) | Get work plan bid ranks for a user|
|[**get_workforcemanagement_workplanbid_preferences**](#get_workforcemanagement_workplanbid_preferences) | Gets an agent&#39;s work plan bidding preference|
|[**get_workforcemanagement_workplanbid_workplans**](#get_workforcemanagement_workplanbid_workplans) | Gets an agent&#39;s work plans for a bid|
|[**get_workforcemanagement_workplanbids**](#get_workforcemanagement_workplanbids) | Gets the list of work plan bids that belong to an agent|
|[**patch_workforcemanagement_agent_adherence_explanation**](#patch_workforcemanagement_agent_adherence_explanation) | Update an adherence explanation|
|[**patch_workforcemanagement_alternativeshifts_trade**](#patch_workforcemanagement_alternativeshifts_trade) | Update my alternative shifts trade by trade ID|
|[**patch_workforcemanagement_alternativeshifts_trades_state_jobs**](#patch_workforcemanagement_alternativeshifts_trades_state_jobs) | Bulk update alternative shift trade states|
|[**patch_workforcemanagement_businessunit**](#patch_workforcemanagement_businessunit) | Update business unit|
|[**patch_workforcemanagement_businessunit_activitycode**](#patch_workforcemanagement_businessunit_activitycode) | Update an activity code|
|[**patch_workforcemanagement_businessunit_activityplan**](#patch_workforcemanagement_businessunit_activityplan) | Update an activity plan|
|[**patch_workforcemanagement_businessunit_alternativeshifts_settings**](#patch_workforcemanagement_businessunit_alternativeshifts_settings) | Update alternative shifts settings for a business unit|
|[**patch_workforcemanagement_businessunit_planninggroup**](#patch_workforcemanagement_businessunit_planninggroup) | Updates the planning group|
|[**patch_workforcemanagement_businessunit_scheduling_run**](#patch_workforcemanagement_businessunit_scheduling_run) | Mark a schedule run as applied|
|[**patch_workforcemanagement_businessunit_servicegoaltemplate**](#patch_workforcemanagement_businessunit_servicegoaltemplate) | Updates a service goal template|
|[**patch_workforcemanagement_businessunit_staffinggroup**](#patch_workforcemanagement_businessunit_staffinggroup) | Updates a staffing group|
|[**patch_workforcemanagement_businessunit_timeoffplan**](#patch_workforcemanagement_businessunit_timeoffplan) | Updates a time-off plan|
|[**patch_workforcemanagement_businessunit_workplanbid**](#patch_workforcemanagement_businessunit_workplanbid) | Update work plan bid|
|[**patch_workforcemanagement_businessunit_workplanbid_group**](#patch_workforcemanagement_businessunit_workplanbid_group) | Update a bid group by bid group Id|
|[**patch_workforcemanagement_businessunit_workplanbid_group_preferences**](#patch_workforcemanagement_businessunit_workplanbid_group_preferences) | Overrides the assigned work plan for the specified agents|
|[**patch_workforcemanagement_managementunit**](#patch_workforcemanagement_managementunit) | Update the requested management unit|
|[**patch_workforcemanagement_managementunit_agents**](#patch_workforcemanagement_managementunit_agents) | Update agent configurations|
|[**patch_workforcemanagement_managementunit_agents_workplans_bulk**](#patch_workforcemanagement_managementunit_agents_workplans_bulk) | Updates agent work plan configuration|
|[**patch_workforcemanagement_managementunit_timeofflimit**](#patch_workforcemanagement_managementunit_timeofflimit) | Updates a time off limit object.|
|[**patch_workforcemanagement_managementunit_timeoffplan**](#patch_workforcemanagement_managementunit_timeoffplan) | Updates a time off plan|
|[**patch_workforcemanagement_managementunit_timeoffrequest_user_integrationstatus**](#patch_workforcemanagement_managementunit_timeoffrequest_user_integrationstatus) | Set integration status for a time off request.|
|[**patch_workforcemanagement_managementunit_user_timeoffrequest**](#patch_workforcemanagement_managementunit_user_timeoffrequest) | Update a time off request|
|[**patch_workforcemanagement_managementunit_week_shifttrade**](#patch_workforcemanagement_managementunit_week_shifttrade) | Updates a shift trade. This route can only be called by the initiating agent|
|[**patch_workforcemanagement_managementunit_workplan**](#patch_workforcemanagement_managementunit_workplan) | Update a work plan|
|[**patch_workforcemanagement_managementunit_workplanrotation**](#patch_workforcemanagement_managementunit_workplanrotation) | Update a work plan rotation|
|[**patch_workforcemanagement_timeoffrequest**](#patch_workforcemanagement_timeoffrequest) | Update a time off request for the current user|
|[**patch_workforcemanagement_user_workplanbidranks**](#patch_workforcemanagement_user_workplanbidranks) | Update work plan bid ranks for a user|
|[**patch_workforcemanagement_users_workplanbidranks_bulk**](#patch_workforcemanagement_users_workplanbidranks_bulk) | Update bulk work plan bid ranks on users. Max 50 users can be updated at a time.|
|[**patch_workforcemanagement_workplanbid_preferences**](#patch_workforcemanagement_workplanbid_preferences) | Update an agent&#39;s work plan bidding preference|
|[**post_workforcemanagement_adherence_explanations**](#post_workforcemanagement_adherence_explanations) | Submit an adherence explanation for the current user|
|[**post_workforcemanagement_adherence_explanations_query**](#post_workforcemanagement_adherence_explanations_query) | Query adherence explanations for the current user|
|[**post_workforcemanagement_adherence_historical**](#post_workforcemanagement_adherence_historical) | Deprecated. Use bulk routes instead (/adherence/historical/bulk)|
|[**post_workforcemanagement_adherence_historical_bulk**](#post_workforcemanagement_adherence_historical_bulk) | Request a historical adherence report in bulk|
|[**post_workforcemanagement_agent_adherence_explanations**](#post_workforcemanagement_agent_adherence_explanations) | Add an adherence explanation for the requested user|
|[**post_workforcemanagement_agent_adherence_explanations_query**](#post_workforcemanagement_agent_adherence_explanations_query) | Query adherence explanations for the given agent across a specified range|
|[**post_workforcemanagement_agents**](#post_workforcemanagement_agents) | Move agents in and out of management unit|
|[**post_workforcemanagement_agents_integrations_hris_query**](#post_workforcemanagement_agents_integrations_hris_query) | Query integrations for agents|
|[**post_workforcemanagement_agents_me_possibleworkshifts**](#post_workforcemanagement_agents_me_possibleworkshifts) | Get agent possible work shifts for requested time frame|
|[**post_workforcemanagement_agentschedules_mine**](#post_workforcemanagement_agentschedules_mine) | Get published schedule for the current user|
|[**post_workforcemanagement_alternativeshifts_offers_jobs**](#post_workforcemanagement_alternativeshifts_offers_jobs) | Request a list of alternative shift offers for a given schedule|
|[**post_workforcemanagement_alternativeshifts_offers_search_jobs**](#post_workforcemanagement_alternativeshifts_offers_search_jobs) | Request a search of alternative shift offers for a given shift|
|[**post_workforcemanagement_alternativeshifts_trades**](#post_workforcemanagement_alternativeshifts_trades) | Create my alternative shift trade using an existing offer&#39;s jobId|
|[**post_workforcemanagement_businessunit_activitycodes**](#post_workforcemanagement_businessunit_activitycodes) | Create a new activity code|
|[**post_workforcemanagement_businessunit_activityplan_runs_jobs**](#post_workforcemanagement_businessunit_activityplan_runs_jobs) | Run an activity plan manually|
|[**post_workforcemanagement_businessunit_activityplans**](#post_workforcemanagement_businessunit_activityplans) | Create an activity plan|
|[**post_workforcemanagement_businessunit_adherence_explanations_query**](#post_workforcemanagement_businessunit_adherence_explanations_query) | Query adherence explanations across an entire business unit for the requested period|
|[**post_workforcemanagement_businessunit_agentschedules_search**](#post_workforcemanagement_businessunit_agentschedules_search) | Search published schedules|
|[**post_workforcemanagement_businessunit_alternativeshifts_trades_search**](#post_workforcemanagement_businessunit_alternativeshifts_trades_search) | List alternative shifts trades for a given management unit or agent|
|[**post_workforcemanagement_businessunit_intraday**](#post_workforcemanagement_businessunit_intraday) | Get intraday data for the given date for the requested planningGroupIds|
|[**post_workforcemanagement_businessunit_planninggroups**](#post_workforcemanagement_businessunit_planninggroups) | Adds a new planning group|
|[**post_workforcemanagement_businessunit_servicegoaltemplates**](#post_workforcemanagement_businessunit_servicegoaltemplates) | Adds a new service goal template|
|[**post_workforcemanagement_businessunit_staffinggroups**](#post_workforcemanagement_businessunit_staffinggroups) | Creates a new staffing group|
|[**post_workforcemanagement_businessunit_staffinggroups_query**](#post_workforcemanagement_businessunit_staffinggroups_query) | Gets staffing group associations for a list of user IDs|
|[**post_workforcemanagement_businessunit_timeofflimits**](#post_workforcemanagement_businessunit_timeofflimits) | Creates a new time-off limit object|
|[**post_workforcemanagement_businessunit_timeofflimits_values_query**](#post_workforcemanagement_businessunit_timeofflimits_values_query) | Retrieves time-off limit related values based on a given set of filters.|
|[**post_workforcemanagement_businessunit_timeoffplans**](#post_workforcemanagement_businessunit_timeoffplans) | Creates a new time-off plan|
|[**post_workforcemanagement_businessunit_week_schedule_agentschedules_query**](#post_workforcemanagement_businessunit_week_schedule_agentschedules_query) | Loads agent schedule data from the schedule. Used in combination with the metadata route|
|[**post_workforcemanagement_businessunit_week_schedule_copy**](#post_workforcemanagement_businessunit_week_schedule_copy) | Copy a schedule|
|[**post_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculations**](#post_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculations) | Request a daily recalculation of the performance prediction for the associated schedule|
|[**post_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculations_uploadurl**](#post_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculations_uploadurl) | Upload daily activity changes to be able to request a performance prediction recalculation|
|[**post_workforcemanagement_businessunit_week_schedule_reschedule**](#post_workforcemanagement_businessunit_week_schedule_reschedule) | Start a rescheduling run|
|[**post_workforcemanagement_businessunit_week_schedule_update**](#post_workforcemanagement_businessunit_week_schedule_update) | Starts processing a schedule update|
|[**post_workforcemanagement_businessunit_week_schedule_update_uploadurl**](#post_workforcemanagement_businessunit_week_schedule_update_uploadurl) | Creates a signed upload URL for updating a schedule|
|[**post_workforcemanagement_businessunit_week_schedules**](#post_workforcemanagement_businessunit_week_schedules) | Create a blank schedule|
|[**post_workforcemanagement_businessunit_week_schedules_generate**](#post_workforcemanagement_businessunit_week_schedules_generate) | Generate a schedule|
|[**post_workforcemanagement_businessunit_week_schedules_import**](#post_workforcemanagement_businessunit_week_schedules_import) | Starts processing a schedule import|
|[**post_workforcemanagement_businessunit_week_schedules_import_uploadurl**](#post_workforcemanagement_businessunit_week_schedules_import_uploadurl) | Creates a signed upload URL for importing a schedule|
|[**post_workforcemanagement_businessunit_week_shorttermforecast_copy**](#post_workforcemanagement_businessunit_week_shorttermforecast_copy) | Copy a short term forecast|
|[**post_workforcemanagement_businessunit_week_shorttermforecasts_generate**](#post_workforcemanagement_businessunit_week_shorttermforecasts_generate) | Generate a short term forecast|
|[**post_workforcemanagement_businessunit_week_shorttermforecasts_import**](#post_workforcemanagement_businessunit_week_shorttermforecasts_import) | Starts importing the uploaded short term forecast|
|[**post_workforcemanagement_businessunit_week_shorttermforecasts_import_uploadurl**](#post_workforcemanagement_businessunit_week_shorttermforecasts_import_uploadurl) | Creates a signed upload URL for importing a short term forecast|
|[**post_workforcemanagement_businessunit_workplanbid_copy**](#post_workforcemanagement_businessunit_workplanbid_copy) | Copy a work plan bid|
|[**post_workforcemanagement_businessunit_workplanbid_groups**](#post_workforcemanagement_businessunit_workplanbid_groups) | Add a bid group in a given work plan bid|
|[**post_workforcemanagement_businessunit_workplanbids**](#post_workforcemanagement_businessunit_workplanbids) | Create a new work plan bid|
|[**post_workforcemanagement_businessunits**](#post_workforcemanagement_businessunits) | Add a new business unit|
|[**post_workforcemanagement_calendar_url_ics**](#post_workforcemanagement_calendar_url_ics) | Create a newly generated calendar link for the current user; if the current user has previously generated one, the generated link will be returned|
|[**post_workforcemanagement_historicaldata_bulk_remove_jobs**](#post_workforcemanagement_historicaldata_bulk_remove_jobs) | Delete the list of the historical data import entries|
|[**post_workforcemanagement_historicaldata_deletejob**](#post_workforcemanagement_historicaldata_deletejob) | Delete the entries of the historical data imports in the organization.|
|[**post_workforcemanagement_historicaldata_validate**](#post_workforcemanagement_historicaldata_validate) | Trigger validation process for historical import|
|[**post_workforcemanagement_integrations_hri_timeofftypes_jobs**](#post_workforcemanagement_integrations_hri_timeofftypes_jobs) | Get list of time off types configured in integration|
|[**post_workforcemanagement_managementunit_agents_workplans_query**](#post_workforcemanagement_managementunit_agents_workplans_query) | Get agents work plans configuration|
|[**post_workforcemanagement_managementunit_agentschedules_search**](#post_workforcemanagement_managementunit_agentschedules_search) | Query published schedules for given given time range for set of users|
|[**post_workforcemanagement_managementunit_historicaladherencequery**](#post_workforcemanagement_managementunit_historicaladherencequery) | Request a historical adherence report|
|[**post_workforcemanagement_managementunit_move**](#post_workforcemanagement_managementunit_move) | Move the requested management unit to a new business unit|
|[**post_workforcemanagement_managementunit_schedules_search**](#post_workforcemanagement_managementunit_schedules_search) | Query published schedules for given given time range for set of users|
|[**post_workforcemanagement_managementunit_shrinkage_jobs**](#post_workforcemanagement_managementunit_shrinkage_jobs) | Request a historical shrinkage report|
|[**post_workforcemanagement_managementunit_timeofflimits**](#post_workforcemanagement_managementunit_timeofflimits) | Creates a new time off limit object under management unit.|
|[**post_workforcemanagement_managementunit_timeofflimits_values_query**](#post_workforcemanagement_managementunit_timeofflimits_values_query) | Retrieves time off limit related values based on a given set of filters.|
|[**post_workforcemanagement_managementunit_timeoffplans**](#post_workforcemanagement_managementunit_timeoffplans) | Creates a new time off plan|
|[**post_workforcemanagement_managementunit_timeoffrequests**](#post_workforcemanagement_managementunit_timeoffrequests) | Create a new time off request|
|[**post_workforcemanagement_managementunit_timeoffrequests_integrationstatus_query**](#post_workforcemanagement_managementunit_timeoffrequests_integrationstatus_query) | Retrieves integration statuses for a list of time off requests|
|[**post_workforcemanagement_managementunit_timeoffrequests_query**](#post_workforcemanagement_managementunit_timeoffrequests_query) | Fetches time off requests matching the conditions specified in the request body|
|[**post_workforcemanagement_managementunit_timeoffrequests_waitlistpositions_query**](#post_workforcemanagement_managementunit_timeoffrequests_waitlistpositions_query) | Retrieves daily waitlist position for a list of time off requests|
|[**post_workforcemanagement_managementunit_user_timeoffbalance_jobs**](#post_workforcemanagement_managementunit_user_timeoffbalance_jobs) | Query time off balances for a given user for specified activity code and dates|
|[**post_workforcemanagement_managementunit_user_timeoffrequest_timeoffbalance_jobs**](#post_workforcemanagement_managementunit_user_timeoffrequest_timeoffbalance_jobs) | Query time off balances for dates spanned by a given time off request|
|[**post_workforcemanagement_managementunit_user_timeoffrequests_estimate**](#post_workforcemanagement_managementunit_user_timeoffrequests_estimate) | Estimates available time off for an agent|
|[**post_workforcemanagement_managementunit_week_shifttrade_match**](#post_workforcemanagement_managementunit_week_shifttrade_match) | Matches a shift trade. This route can only be called by the receiving agent|
|[**post_workforcemanagement_managementunit_week_shifttrades**](#post_workforcemanagement_managementunit_week_shifttrades) | Adds a shift trade|
|[**post_workforcemanagement_managementunit_week_shifttrades_search**](#post_workforcemanagement_managementunit_week_shifttrades_search) | Searches for potential shift trade matches for the current agent|
|[**post_workforcemanagement_managementunit_week_shifttrades_state_bulk**](#post_workforcemanagement_managementunit_week_shifttrades_state_bulk) | Updates the state of a batch of shift trades|
|[**post_workforcemanagement_managementunit_workplan_copy**](#post_workforcemanagement_managementunit_workplan_copy) | Create a copy of work plan|
|[**post_workforcemanagement_managementunit_workplan_validate**](#post_workforcemanagement_managementunit_workplan_validate) | Validate Work Plan|
|[**post_workforcemanagement_managementunit_workplanrotation_copy**](#post_workforcemanagement_managementunit_workplanrotation_copy) | Create a copy of work plan rotation|
|[**post_workforcemanagement_managementunit_workplanrotations**](#post_workforcemanagement_managementunit_workplanrotations) | Create a new work plan rotation|
|[**post_workforcemanagement_managementunit_workplans**](#post_workforcemanagement_managementunit_workplans) | Create a new work plan|
|[**post_workforcemanagement_managementunits**](#post_workforcemanagement_managementunits) | Add a management unit|
|[**post_workforcemanagement_notifications_update**](#post_workforcemanagement_notifications_update) | Mark a list of notifications as read or unread|
|[**post_workforcemanagement_schedules**](#post_workforcemanagement_schedules) | Get published schedule for the current user|
|[**post_workforcemanagement_team_adherence_historical**](#post_workforcemanagement_team_adherence_historical) | Request a teams historical adherence report|
|[**post_workforcemanagement_team_shrinkage_jobs**](#post_workforcemanagement_team_shrinkage_jobs) | Request a historical shrinkage report|
|[**post_workforcemanagement_timeoffbalance_jobs**](#post_workforcemanagement_timeoffbalance_jobs) | Query time off balances for the current user for specified activity code and dates|
|[**post_workforcemanagement_timeofflimits_available_query**](#post_workforcemanagement_timeofflimits_available_query) | Queries available time off for the current user|
|[**post_workforcemanagement_timeoffrequests**](#post_workforcemanagement_timeoffrequests) | Create a time off request for the current user|
|[**post_workforcemanagement_timeoffrequests_estimate**](#post_workforcemanagement_timeoffrequests_estimate) | Estimates available time off for current user|
|[**post_workforcemanagement_timeoffrequests_integrationstatus_query**](#post_workforcemanagement_timeoffrequests_integrationstatus_query) | Retrieves integration statuses for a list of current user time off requests|
|[**put_workforcemanagement_agent_integrations_hris**](#put_workforcemanagement_agent_integrations_hris) | Update integrations for agent|
|[**put_workforcemanagement_businessunit_timeofflimit_values**](#put_workforcemanagement_businessunit_timeofflimit_values) | Sets daily values for a date range of time-off limit object|
|[**put_workforcemanagement_managementunit_timeofflimit_values**](#put_workforcemanagement_managementunit_timeofflimit_values) | Sets daily values for a date range of time off limit object|



## delete_workforcemanagement_businessunit

>  delete_workforcemanagement_businessunit(business_unit_id)


Delete business unit

A business unit cannot be deleted if it contains one or more management units

Wraps DELETE /api/v2/workforcemanagement/businessunits/{businessUnitId} 

Requires ANY permissions: 

* wfm:businessUnit:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit, or 'mine' for the business unit of the logged-in user.

try:
    # Delete business unit
    api_instance.delete_workforcemanagement_businessunit(business_unit_id)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->delete_workforcemanagement_businessunit: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit, or &#39;mine&#39; for the business unit of the logged-in user. |  |

### Return type

void (empty response body)


## delete_workforcemanagement_businessunit_activitycode

>  delete_workforcemanagement_businessunit_activitycode(business_unit_id, activity_code_id)


Deletes an activity code

Wraps DELETE /api/v2/workforcemanagement/businessunits/{businessUnitId}/activitycodes/{activityCodeId} 

Requires ANY permissions: 

* wfm:activityCode:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit, or 'mine' for the business unit of the logged-in user.
activity_code_id = 'activity_code_id_example' # str | The ID of the activity code to delete

try:
    # Deletes an activity code
    api_instance.delete_workforcemanagement_businessunit_activitycode(business_unit_id, activity_code_id)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->delete_workforcemanagement_businessunit_activitycode: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit, or &#39;mine&#39; for the business unit of the logged-in user. |  |
| **activity_code_id** | **str**| The ID of the activity code to delete |  |

### Return type

void (empty response body)


## delete_workforcemanagement_businessunit_planninggroup

>  delete_workforcemanagement_businessunit_planninggroup(business_unit_id, planning_group_id)


Deletes the planning group

Wraps DELETE /api/v2/workforcemanagement/businessunits/{businessUnitId}/planninggroups/{planningGroupId} 

Requires ANY permissions: 

* wfm:planningGroup:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit.
planning_group_id = 'planning_group_id_example' # str | The ID of a planning group to delete

try:
    # Deletes the planning group
    api_instance.delete_workforcemanagement_businessunit_planninggroup(business_unit_id, planning_group_id)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->delete_workforcemanagement_businessunit_planninggroup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit. |  |
| **planning_group_id** | **str**| The ID of a planning group to delete |  |

### Return type

void (empty response body)


## delete_workforcemanagement_businessunit_scheduling_run

>  delete_workforcemanagement_businessunit_scheduling_run(business_unit_id, run_id)


Cancel a scheduling run

Wraps DELETE /api/v2/workforcemanagement/businessunits/{businessUnitId}/scheduling/runs/{runId} 

Requires ANY permissions: 

* wfm:schedule:generate

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
run_id = 'run_id_example' # str | The ID of the schedule run

try:
    # Cancel a scheduling run
    api_instance.delete_workforcemanagement_businessunit_scheduling_run(business_unit_id, run_id)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->delete_workforcemanagement_businessunit_scheduling_run: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **run_id** | **str**| The ID of the schedule run |  |

### Return type

void (empty response body)


## delete_workforcemanagement_businessunit_servicegoaltemplate

>  delete_workforcemanagement_businessunit_servicegoaltemplate(business_unit_id, service_goal_template_id)


Delete a service goal template

Wraps DELETE /api/v2/workforcemanagement/businessunits/{businessUnitId}/servicegoaltemplates/{serviceGoalTemplateId} 

Requires ANY permissions: 

* wfm:serviceGoalTemplate:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit.
service_goal_template_id = 'service_goal_template_id_example' # str | The ID of the service goal template to delete

try:
    # Delete a service goal template
    api_instance.delete_workforcemanagement_businessunit_servicegoaltemplate(business_unit_id, service_goal_template_id)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->delete_workforcemanagement_businessunit_servicegoaltemplate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit. |  |
| **service_goal_template_id** | **str**| The ID of the service goal template to delete |  |

### Return type

void (empty response body)


## delete_workforcemanagement_businessunit_staffinggroup

>  delete_workforcemanagement_businessunit_staffinggroup(business_unit_id, staffing_group_id)


Deletes a staffing group

Wraps DELETE /api/v2/workforcemanagement/businessunits/{businessUnitId}/staffinggroups/{staffingGroupId} 

Requires ANY permissions: 

* wfm:staffingGroup:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
staffing_group_id = 'staffing_group_id_example' # str | The ID of the staffing group to delete

try:
    # Deletes a staffing group
    api_instance.delete_workforcemanagement_businessunit_staffinggroup(business_unit_id, staffing_group_id)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->delete_workforcemanagement_businessunit_staffinggroup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **staffing_group_id** | **str**| The ID of the staffing group to delete |  |

### Return type

void (empty response body)


## delete_workforcemanagement_businessunit_timeofflimit

>  delete_workforcemanagement_businessunit_timeofflimit(business_unit_id, time_off_limit_id)


Deletes a time-off limit object

Wraps DELETE /api/v2/workforcemanagement/businessunits/{businessUnitId}/timeofflimits/{timeOffLimitId} 

Requires ANY permissions: 

* wfm:timeOffLimit:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
time_off_limit_id = 'time_off_limit_id_example' # str | The ID of the time-off limit object to delete

try:
    # Deletes a time-off limit object
    api_instance.delete_workforcemanagement_businessunit_timeofflimit(business_unit_id, time_off_limit_id)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->delete_workforcemanagement_businessunit_timeofflimit: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **time_off_limit_id** | **str**| The ID of the time-off limit object to delete |  |

### Return type

void (empty response body)


## delete_workforcemanagement_businessunit_timeoffplan

>  delete_workforcemanagement_businessunit_timeoffplan(business_unit_id, time_off_plan_id)


Deletes a time-off plan

Wraps DELETE /api/v2/workforcemanagement/businessunits/{businessUnitId}/timeoffplans/{timeOffPlanId} 

Requires ANY permissions: 

* wfm:timeOffPlan:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
time_off_plan_id = 'time_off_plan_id_example' # str | The ID of the time-off plan to delete

try:
    # Deletes a time-off plan
    api_instance.delete_workforcemanagement_businessunit_timeoffplan(business_unit_id, time_off_plan_id)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->delete_workforcemanagement_businessunit_timeoffplan: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **time_off_plan_id** | **str**| The ID of the time-off plan to delete |  |

### Return type

void (empty response body)


## delete_workforcemanagement_businessunit_week_schedule

> [**BuAsyncScheduleResponse**](BuAsyncScheduleResponse) delete_workforcemanagement_businessunit_week_schedule(business_unit_id, week_id, schedule_id)


Delete a schedule

Wraps DELETE /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId} 

Requires ANY permissions: 

* wfm:schedule:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
week_id = '2013-10-20' # date | First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
schedule_id = 'schedule_id_example' # str | The ID of the schedule

try:
    # Delete a schedule
    api_response = api_instance.delete_workforcemanagement_businessunit_week_schedule(business_unit_id, week_id, schedule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->delete_workforcemanagement_businessunit_week_schedule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **week_id** | **date**| First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **schedule_id** | **str**| The ID of the schedule |  |

### Return type

[**BuAsyncScheduleResponse**](BuAsyncScheduleResponse)


## delete_workforcemanagement_businessunit_week_shorttermforecast

>  delete_workforcemanagement_businessunit_week_shorttermforecast(business_unit_id, week_date_id, forecast_id)


Delete a short term forecast

Must not be tied to any schedules

Wraps DELETE /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekDateId}/shorttermforecasts/{forecastId} 

Requires ANY permissions: 

* wfm:shortTermForecast:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit to which the forecast belongs
week_date_id = '2013-10-20' # date | The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
forecast_id = 'forecast_id_example' # str | The ID of the forecast

try:
    # Delete a short term forecast
    api_instance.delete_workforcemanagement_businessunit_week_shorttermforecast(business_unit_id, week_date_id, forecast_id)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->delete_workforcemanagement_businessunit_week_shorttermforecast: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit to which the forecast belongs |  |
| **week_date_id** | **date**| The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **forecast_id** | **str**| The ID of the forecast |  |

### Return type

void (empty response body)


## delete_workforcemanagement_businessunit_workplanbid

>  delete_workforcemanagement_businessunit_workplanbid(business_unit_id, bid_id)


Delete a work plan bid

Wraps DELETE /api/v2/workforcemanagement/businessunits/{businessUnitId}/workplanbids/{bidId} 

Requires ANY permissions: 

* wfm:workPlanBid:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
bid_id = 'bid_id_example' # str | The ID of the work plan bid

try:
    # Delete a work plan bid
    api_instance.delete_workforcemanagement_businessunit_workplanbid(business_unit_id, bid_id)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->delete_workforcemanagement_businessunit_workplanbid: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **bid_id** | **str**| The ID of the work plan bid |  |

### Return type

void (empty response body)


## delete_workforcemanagement_businessunit_workplanbid_group

>  delete_workforcemanagement_businessunit_workplanbid_group(business_unit_id, bid_id, bid_group_id)


Delete a bid group by bid group Id

Wraps DELETE /api/v2/workforcemanagement/businessunits/{businessUnitId}/workplanbids/{bidId}/groups/{bidGroupId} 

Requires ANY permissions: 

* wfm:workPlanBidGroup:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
bid_id = 'bid_id_example' # str | The work plan bid id of the bid groups
bid_group_id = 'bid_group_id_example' # str | Work Plan Bid Group id

try:
    # Delete a bid group by bid group Id
    api_instance.delete_workforcemanagement_businessunit_workplanbid_group(business_unit_id, bid_id, bid_group_id)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->delete_workforcemanagement_businessunit_workplanbid_group: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **bid_id** | **str**| The work plan bid id of the bid groups |  |
| **bid_group_id** | **str**| Work Plan Bid Group id |  |

### Return type

void (empty response body)


## delete_workforcemanagement_calendar_url_ics

>  delete_workforcemanagement_calendar_url_ics()


Disable generated calendar link for the current user

Wraps DELETE /api/v2/workforcemanagement/calendar/url/ics 

Requires ALL permissions: 

* wfm:agentSchedule:sync

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()

try:
    # Disable generated calendar link for the current user
    api_instance.delete_workforcemanagement_calendar_url_ics()
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->delete_workforcemanagement_calendar_url_ics: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

void (empty response body)


## delete_workforcemanagement_managementunit

>  delete_workforcemanagement_managementunit(management_unit_id)


Delete management unit

Wraps DELETE /api/v2/workforcemanagement/managementunits/{managementUnitId} 

Requires ANY permissions: 

* wfm:managementUnit:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.

try:
    # Delete management unit
    api_instance.delete_workforcemanagement_managementunit(management_unit_id)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->delete_workforcemanagement_managementunit: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |

### Return type

void (empty response body)


## delete_workforcemanagement_managementunit_timeofflimit

>  delete_workforcemanagement_managementunit_timeofflimit(management_unit_id, time_off_limit_id)


Deletes a time off limit object

Wraps DELETE /api/v2/workforcemanagement/managementunits/{managementUnitId}/timeofflimits/{timeOffLimitId} 

Requires ANY permissions: 

* wfm:timeOffLimit:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit.
time_off_limit_id = 'time_off_limit_id_example' # str | The ID of the time off limit object to delete

try:
    # Deletes a time off limit object
    api_instance.delete_workforcemanagement_managementunit_timeofflimit(management_unit_id, time_off_limit_id)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->delete_workforcemanagement_managementunit_timeofflimit: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit. |  |
| **time_off_limit_id** | **str**| The ID of the time off limit object to delete |  |

### Return type

void (empty response body)


## delete_workforcemanagement_managementunit_timeoffplan

>  delete_workforcemanagement_managementunit_timeoffplan(management_unit_id, time_off_plan_id)


Deletes a time off plan

Wraps DELETE /api/v2/workforcemanagement/managementunits/{managementUnitId}/timeoffplans/{timeOffPlanId} 

Requires ANY permissions: 

* wfm:timeOffPlan:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit
time_off_plan_id = 'time_off_plan_id_example' # str | The ID of the time off plan to delete

try:
    # Deletes a time off plan
    api_instance.delete_workforcemanagement_managementunit_timeoffplan(management_unit_id, time_off_plan_id)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->delete_workforcemanagement_managementunit_timeoffplan: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit |  |
| **time_off_plan_id** | **str**| The ID of the time off plan to delete |  |

### Return type

void (empty response body)


## delete_workforcemanagement_managementunit_workplan

>  delete_workforcemanagement_managementunit_workplan(management_unit_id, work_plan_id)


Delete a work plan

Wraps DELETE /api/v2/workforcemanagement/managementunits/{managementUnitId}/workplans/{workPlanId} 

Requires ANY permissions: 

* wfm:workPlan:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
work_plan_id = 'work_plan_id_example' # str | The ID of the work plan to delete

try:
    # Delete a work plan
    api_instance.delete_workforcemanagement_managementunit_workplan(management_unit_id, work_plan_id)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->delete_workforcemanagement_managementunit_workplan: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **work_plan_id** | **str**| The ID of the work plan to delete |  |

### Return type

void (empty response body)


## delete_workforcemanagement_managementunit_workplanrotation

>  delete_workforcemanagement_managementunit_workplanrotation(management_unit_id, work_plan_rotation_id)


Delete a work plan rotation

Wraps DELETE /api/v2/workforcemanagement/managementunits/{managementUnitId}/workplanrotations/{workPlanRotationId} 

Requires ANY permissions: 

* wfm:workPlanRotation:delete

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
work_plan_rotation_id = 'work_plan_rotation_id_example' # str | The ID of the work plan rotation to be deleted

try:
    # Delete a work plan rotation
    api_instance.delete_workforcemanagement_managementunit_workplanrotation(management_unit_id, work_plan_rotation_id)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->delete_workforcemanagement_managementunit_workplanrotation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **work_plan_rotation_id** | **str**| The ID of the work plan rotation to be deleted |  |

### Return type

void (empty response body)


## get_workforcemanagement_adherence

> [**list[UserScheduleAdherence]**](UserScheduleAdherence) get_workforcemanagement_adherence(user_id)


Get a list of UserScheduleAdherence records for the requested users

Wraps GET /api/v2/workforcemanagement/adherence 

Requires ANY permissions: 

* wfm:realtimeAdherence:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
user_id = ['user_id_example'] # list[str] | User Id(s) for which to fetch current schedule adherence information.  Min 1, Max of 100 userIds per request

try:
    # Get a list of UserScheduleAdherence records for the requested users
    api_response = api_instance.get_workforcemanagement_adherence(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_adherence: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | [**list[str]**](str)| User Id(s) for which to fetch current schedule adherence information.  Min 1, Max of 100 userIds per request |  |

### Return type

[**list[UserScheduleAdherence]**](UserScheduleAdherence)


## get_workforcemanagement_adherence_explanation

> [**AdherenceExplanationResponse**](AdherenceExplanationResponse) get_workforcemanagement_adherence_explanation(explanation_id)


Get an adherence explanation for the current user

Wraps GET /api/v2/workforcemanagement/adherence/explanations/{explanationId} 

Requires ANY permissions: 

* wfm:agentAdherenceExplanation:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
explanation_id = 'explanation_id_example' # str | The ID of the explanation to update

try:
    # Get an adherence explanation for the current user
    api_response = api_instance.get_workforcemanagement_adherence_explanation(explanation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_adherence_explanation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **explanation_id** | **str**| The ID of the explanation to update |  |

### Return type

[**AdherenceExplanationResponse**](AdherenceExplanationResponse)


## get_workforcemanagement_adherence_explanations_job

> [**AdherenceExplanationJob**](AdherenceExplanationJob) get_workforcemanagement_adherence_explanations_job(job_id)


Query the status of an adherence explanation operation. Only the user who started the operation can query the status

Job details are only retained if the initial request returned a 202 ACCEPTED response

Wraps GET /api/v2/workforcemanagement/adherence/explanations/jobs/{jobId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
job_id = 'job_id_example' # str | The ID of the job

try:
    # Query the status of an adherence explanation operation. Only the user who started the operation can query the status
    api_response = api_instance.get_workforcemanagement_adherence_explanations_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_adherence_explanations_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| The ID of the job |  |

### Return type

[**AdherenceExplanationJob**](AdherenceExplanationJob)


## get_workforcemanagement_adherence_historical_bulk_job

> [**WfmHistoricalAdherenceBulkResponse**](WfmHistoricalAdherenceBulkResponse) get_workforcemanagement_adherence_historical_bulk_job(job_id)


Request to fetch the status of the historical adherence bulk job. Only the user who started the operation can query the status

Job details are only retained if the initial request returned a 202 ACCEPTED response

Wraps GET /api/v2/workforcemanagement/adherence/historical/bulk/jobs/{jobId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
job_id = 'job_id_example' # str | ID of the job to get

try:
    # Request to fetch the status of the historical adherence bulk job. Only the user who started the operation can query the status
    api_response = api_instance.get_workforcemanagement_adherence_historical_bulk_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_adherence_historical_bulk_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| ID of the job to get |  |

### Return type

[**WfmHistoricalAdherenceBulkResponse**](WfmHistoricalAdherenceBulkResponse)


## get_workforcemanagement_adherence_historical_job

> [**WfmHistoricalAdherenceResponse**](WfmHistoricalAdherenceResponse) get_workforcemanagement_adherence_historical_job(job_id)


Query the status of a historical adherence request operation. Only the user who started the operation can query the status

Job details are only retained if the initial request returned a 202 ACCEPTED response

Wraps GET /api/v2/workforcemanagement/adherence/historical/jobs/{jobId} 

Requires ANY permissions: 

* wfm:historicalAdherence:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
job_id = 'job_id_example' # str | jobId

try:
    # Query the status of a historical adherence request operation. Only the user who started the operation can query the status
    api_response = api_instance.get_workforcemanagement_adherence_historical_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_adherence_historical_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

[**WfmHistoricalAdherenceResponse**](WfmHistoricalAdherenceResponse)


## get_workforcemanagement_agent_adherence_explanation

> [**AdherenceExplanationResponse**](AdherenceExplanationResponse) get_workforcemanagement_agent_adherence_explanation(agent_id, explanation_id)


Get an adherence explanation

Wraps GET /api/v2/workforcemanagement/agents/{agentId}/adherence/explanations/{explanationId} 

Requires ANY permissions: 

* wfm:adherenceExplanation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
agent_id = 'agent_id_example' # str | The ID of the agent to query
explanation_id = 'explanation_id_example' # str | The ID of the explanation to update

try:
    # Get an adherence explanation
    api_response = api_instance.get_workforcemanagement_agent_adherence_explanation(agent_id, explanation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_agent_adherence_explanation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str**| The ID of the agent to query |  |
| **explanation_id** | **str**| The ID of the explanation to update |  |

### Return type

[**AdherenceExplanationResponse**](AdherenceExplanationResponse)


## get_workforcemanagement_agent_managementunit

> [**AgentManagementUnitReference**](AgentManagementUnitReference) get_workforcemanagement_agent_managementunit(agent_id)


Get the management unit to which the agent belongs

Wraps GET /api/v2/workforcemanagement/agents/{agentId}/managementunit 

Requires ANY permissions: 

* wfm:agent:view
* wfm:publishedSchedule:view
* wfm:schedule:view
* coaching:appointment:add
* coaching:appointment:edit
* learning:assignment:add
* learning:assignment:reschedule

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
agent_id = 'agent_id_example' # str | The ID of the agent to look up

try:
    # Get the management unit to which the agent belongs
    api_response = api_instance.get_workforcemanagement_agent_managementunit(agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_agent_managementunit: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str**| The ID of the agent to look up |  |

### Return type

[**AgentManagementUnitReference**](AgentManagementUnitReference)


## get_workforcemanagement_agents_me_managementunit

> [**AgentManagementUnitReference**](AgentManagementUnitReference) get_workforcemanagement_agents_me_managementunit()


Get the management unit to which the currently logged in agent belongs

Wraps GET /api/v2/workforcemanagement/agents/me/managementunit 

Requires ANY permissions: 

* wfm:agentSchedule:view
* wfm:agentTimeOffRequest:submit
* wfm:activityCode:add
* wfm:activityCode:delete
* wfm:activityCode:edit
* wfm:activityCode:view
* wfm:agent:edit
* wfm:agent:view
* wfm:businessUnit:add
* wfm:businessUnit:delete
* wfm:businessUnit:edit
* wfm:businessUnit:view
* wfm:historicalAdherence:view
* wfm:intraday:view
* wfm:managementUnit:add
* wfm:managementUnit:delete
* wfm:managementUnit:edit
* wfm:managementUnit:view
* wfm:realtimeAdherence:view
* wfm:schedule:add
* wfm:schedule:delete
* wfm:schedule:edit
* wfm:schedule:generate
* wfm:schedule:view
* wfm:publishedSchedule:view
* wfm:serviceGoalTemplate:add
* wfm:serviceGoalTemplate:delete
* wfm:serviceGoalTemplate:edit
* wfm:serviceGoalTemplate:view
* wfm:planningGroup:add
* wfm:planningGroup:delete
* wfm:planningGroup:edit
* wfm:planningGroup:view
* wfm:shiftTradeRequest:edit
* wfm:shiftTradeRequest:view
* wfm:shortTermForecast:add
* wfm:shortTermForecast:delete
* wfm:shortTermForecast:edit
* wfm:shortTermForecast:view
* wfm:timeOffLimit:add
* wfm:timeOffLimit:delete
* wfm:timeOffLimit:edit
* wfm:timeOffLimit:view
* wfm:timeOffPlan:add
* wfm:timeOffPlan:delete
* wfm:timeOffPlan:edit
* wfm:timeOffPlan:view
* wfm:timeOffRequest:add
* wfm:timeOffRequest:edit
* wfm:timeOffRequest:view
* wfm:workPlan:add
* wfm:workPlan:delete
* wfm:workPlan:edit
* wfm:workPlan:view
* wfm:workPlanRotation:add
* wfm:workPlanRotation:delete
* wfm:workPlanRotation:edit
* wfm:workPlanRotation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()

try:
    # Get the management unit to which the currently logged in agent belongs
    api_response = api_instance.get_workforcemanagement_agents_me_managementunit()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_agents_me_managementunit: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**AgentManagementUnitReference**](AgentManagementUnitReference)


## get_workforcemanagement_alternativeshifts_offers_job

> [**AlternativeShiftJobResponse**](AlternativeShiftJobResponse) get_workforcemanagement_alternativeshifts_offers_job(job_id)


Query the status of an alternative shift offers operation. Only the user who started the operation can query the status

Job details are only retained if the initial request returned a 202 ACCEPTED response

Wraps GET /api/v2/workforcemanagement/alternativeshifts/offers/jobs/{jobId} 

Requires ANY permissions: 

* wfm:agentAlternativeShift:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
job_id = 'job_id_example' # str | The ID of the job

try:
    # Query the status of an alternative shift offers operation. Only the user who started the operation can query the status
    api_response = api_instance.get_workforcemanagement_alternativeshifts_offers_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_alternativeshifts_offers_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| The ID of the job |  |

### Return type

[**AlternativeShiftJobResponse**](AlternativeShiftJobResponse)


## get_workforcemanagement_alternativeshifts_offers_search_job

> [**AlternativeShiftJobResponse**](AlternativeShiftJobResponse) get_workforcemanagement_alternativeshifts_offers_search_job(job_id)


Query the status of an alternative shift search offers operation. Only the user who started the operation can query the status

Job details are only retained if the initial request returned a 202 ACCEPTED response

Wraps GET /api/v2/workforcemanagement/alternativeshifts/offers/search/jobs/{jobId} 

Requires ANY permissions: 

* wfm:agentAlternativeShift:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
job_id = 'job_id_example' # str | The ID of the job

try:
    # Query the status of an alternative shift search offers operation. Only the user who started the operation can query the status
    api_response = api_instance.get_workforcemanagement_alternativeshifts_offers_search_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_alternativeshifts_offers_search_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| The ID of the job |  |

### Return type

[**AlternativeShiftJobResponse**](AlternativeShiftJobResponse)


## get_workforcemanagement_alternativeshifts_settings

> [**AlternativeShiftBuSettingsResponse**](AlternativeShiftBuSettingsResponse) get_workforcemanagement_alternativeshifts_settings()


Get alternative shifts settings from the current logged in agent’s business unit

Wraps GET /api/v2/workforcemanagement/alternativeshifts/settings 

Requires ANY permissions: 

* wfm:agentAlternativeShift:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()

try:
    # Get alternative shifts settings from the current logged in agent’s business unit
    api_response = api_instance.get_workforcemanagement_alternativeshifts_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_alternativeshifts_settings: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**AlternativeShiftBuSettingsResponse**](AlternativeShiftBuSettingsResponse)


## get_workforcemanagement_alternativeshifts_trade

> [**AlternativeShiftTradeResponse**](AlternativeShiftTradeResponse) get_workforcemanagement_alternativeshifts_trade(trade_id)


Get my alternative shift trade by trade ID

Wraps GET /api/v2/workforcemanagement/alternativeshifts/trades/{tradeId} 

Requires ANY permissions: 

* wfm:agentAlternativeShift:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
trade_id = 'trade_id_example' # str | The ID of the alternative shift trade

try:
    # Get my alternative shift trade by trade ID
    api_response = api_instance.get_workforcemanagement_alternativeshifts_trade(trade_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_alternativeshifts_trade: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trade_id** | **str**| The ID of the alternative shift trade |  |

### Return type

[**AlternativeShiftTradeResponse**](AlternativeShiftTradeResponse)


## get_workforcemanagement_alternativeshifts_trades

> [**ListAlternativeShiftTradesResponse**](ListAlternativeShiftTradesResponse) get_workforcemanagement_alternativeshifts_trades(force_async=force_async)


Get a list of my alternative shifts trades

Wraps GET /api/v2/workforcemanagement/alternativeshifts/trades 

Requires ANY permissions: 

* wfm:agentAlternativeShift:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
force_async = True # bool | Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes (optional)

try:
    # Get a list of my alternative shifts trades
    api_response = api_instance.get_workforcemanagement_alternativeshifts_trades(force_async=force_async)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_alternativeshifts_trades: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **force_async** | **bool**| Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes | [optional]  |

### Return type

[**ListAlternativeShiftTradesResponse**](ListAlternativeShiftTradesResponse)


## get_workforcemanagement_alternativeshifts_trades_job

> [**AlternativeShiftJobResponse**](AlternativeShiftJobResponse) get_workforcemanagement_alternativeshifts_trades_job(job_id)


Query the status of an alternative shift trades operation. Only the user who started the operation can query the status

Job details are only retained if the initial request returned a 202 ACCEPTED response

Wraps GET /api/v2/workforcemanagement/alternativeshifts/trades/jobs/{jobId} 

Requires ANY permissions: 

* wfm:agentAlternativeShift:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
job_id = 'job_id_example' # str | The ID of the job

try:
    # Query the status of an alternative shift trades operation. Only the user who started the operation can query the status
    api_response = api_instance.get_workforcemanagement_alternativeshifts_trades_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_alternativeshifts_trades_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| The ID of the job |  |

### Return type

[**AlternativeShiftJobResponse**](AlternativeShiftJobResponse)


## get_workforcemanagement_alternativeshifts_trades_state_job

> [**AlternativeShiftJobResponse**](AlternativeShiftJobResponse) get_workforcemanagement_alternativeshifts_trades_state_job(job_id)


Query the status of an alternative shift trade state operation. Only the user who started the operation can query the status

Job details are only retained if the initial request returned a 202 ACCEPTED response

Wraps GET /api/v2/workforcemanagement/alternativeshifts/trades/state/jobs/{jobId} 

Requires ANY permissions: 

* wfm:alternativeShift:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
job_id = 'job_id_example' # str | The ID of the job

try:
    # Query the status of an alternative shift trade state operation. Only the user who started the operation can query the status
    api_response = api_instance.get_workforcemanagement_alternativeshifts_trades_state_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_alternativeshifts_trades_state_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| The ID of the job |  |

### Return type

[**AlternativeShiftJobResponse**](AlternativeShiftJobResponse)


## get_workforcemanagement_businessunit

> [**BusinessUnitResponse**](BusinessUnitResponse) get_workforcemanagement_businessunit(business_unit_id, expand=expand)


Get business unit

Expanding \"settings\" will retrieve all settings.  All other expands will retrieve only the requested settings field(s).

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId} 

Requires ANY permissions: 

* wfm:activityCode:add
* wfm:activityCode:delete
* wfm:activityCode:edit
* wfm:activityCode:view
* wfm:agent:edit
* wfm:agentSchedule:view
* wfm:agentTimeOffRequest:submit
* wfm:agent:view
* wfm:businessUnit:add
* wfm:businessUnit:delete
* wfm:businessUnit:edit
* wfm:businessUnit:view
* wfm:historicalAdherence:view
* wfm:shrinkage:view
* wfm:intraday:view
* wfm:managementUnit:add
* wfm:managementUnit:delete
* wfm:managementUnit:edit
* wfm:managementUnit:view
* wfm:publishedSchedule:view
* wfm:realtimeAdherence:view
* wfm:schedule:add
* wfm:schedule:delete
* wfm:schedule:edit
* wfm:schedule:generate
* wfm:schedule:view
* wfm:serviceGoalTemplate:add
* wfm:serviceGoalTemplate:delete
* wfm:serviceGoalTemplate:edit
* wfm:serviceGoalTemplate:view
* wfm:planningGroup:add
* wfm:planningGroup:delete
* wfm:planningGroup:edit
* wfm:planningGroup:view
* wfm:shiftTradeRequest:edit
* wfm:shiftTradeRequest:view
* wfm:agentShiftTradeRequest:participate
* wfm:shortTermForecast:add
* wfm:shortTermForecast:delete
* wfm:shortTermForecast:edit
* wfm:shortTermForecast:view
* wfm:staffingGroup:add
* wfm:staffingGroup:delete
* wfm:staffingGroup:edit
* wfm:staffingGroup:view
* wfm:timeOffRequest:add
* wfm:timeOffRequest:edit
* wfm:timeOffRequest:view
* wfm:timeOffLimit:add
* wfm:timeOffLimit:delete
* wfm:timeOffLimit:edit
* wfm:timeOffLimit:view
* wfm:timeOffPlan:add
* wfm:timeOffPlan:delete
* wfm:timeOffPlan:edit
* wfm:timeOffPlan:view
* wfm:timeOffRequest:add
* wfm:timeOffRequest:edit
* wfm:timeOffRequest:view
* wfm:workPlan:add
* wfm:workPlan:delete
* wfm:workPlan:edit
* wfm:workPlan:view
* wfm:workPlanRotation:add
* wfm:workPlanRotation:delete
* wfm:workPlanRotation:edit
* wfm:workPlanRotation:view
* coaching:appointment:add
* coaching:appointment:edit
* learning:assignment:add
* learning:assignment:reschedule

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit, or 'mine' for the business unit of the logged-in user.
expand = ['expand_example'] # list[str] | Include to access additional data on the business unit (optional)

try:
    # Get business unit
    api_response = api_instance.get_workforcemanagement_businessunit(business_unit_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit, or &#39;mine&#39; for the business unit of the logged-in user. |  |
| **expand** | [**list[str]**](str)| Include to access additional data on the business unit | [optional] <br />**Values**: settings, settings.timeZone, settings.startDayOfWeek, settings.shortTermForecasting, settings.scheduling, settings.notifications.scheduling, settings.learning, settings.coaching |

### Return type

[**BusinessUnitResponse**](BusinessUnitResponse)


## get_workforcemanagement_businessunit_activitycode

> [**BusinessUnitActivityCode**](BusinessUnitActivityCode) get_workforcemanagement_businessunit_activitycode(business_unit_id, activity_code_id)


Get an activity code

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/activitycodes/{activityCodeId} 

Requires ANY permissions: 

* wfm:activityCode:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit, or 'mine' for the business unit of the logged-in user.
activity_code_id = 'activity_code_id_example' # str | The ID of the activity code to fetch

try:
    # Get an activity code
    api_response = api_instance.get_workforcemanagement_businessunit_activitycode(business_unit_id, activity_code_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_activitycode: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit, or &#39;mine&#39; for the business unit of the logged-in user. |  |
| **activity_code_id** | **str**| The ID of the activity code to fetch |  |

### Return type

[**BusinessUnitActivityCode**](BusinessUnitActivityCode)


## get_workforcemanagement_businessunit_activitycodes

> [**BusinessUnitActivityCodeListing**](BusinessUnitActivityCodeListing) get_workforcemanagement_businessunit_activitycodes(business_unit_id, force_download_service=force_download_service)


Get activity codes

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/activitycodes 

Requires ANY permissions: 

* wfm:agentSchedule:view
* wfm:agentTimeOffRequest:submit
* wfm:activityCode:add
* wfm:activityCode:delete
* wfm:activityCode:edit
* wfm:activityCode:view
* wfm:agent:edit
* wfm:agent:view
* wfm:businessUnit:add
* wfm:businessUnit:delete
* wfm:businessUnit:edit
* wfm:businessUnit:view
* wfm:historicalAdherence:view
* wfm:shrinkage:view
* wfm:intraday:view
* wfm:managementUnit:add
* wfm:managementUnit:delete
* wfm:managementUnit:edit
* wfm:managementUnit:view
* wfm:realtimeAdherence:view
* wfm:schedule:add
* wfm:schedule:delete
* wfm:schedule:edit
* wfm:schedule:generate
* wfm:schedule:view
* wfm:publishedSchedule:view
* wfm:serviceGoalTemplate:add
* wfm:serviceGoalTemplate:delete
* wfm:serviceGoalTemplate:edit
* wfm:serviceGoalTemplate:view
* wfm:planningGroup:add
* wfm:planningGroup:delete
* wfm:planningGroup:edit
* wfm:planningGroup:view
* wfm:shiftTradeRequest:edit
* wfm:shiftTradeRequest:view
* wfm:shortTermForecast:add
* wfm:shortTermForecast:delete
* wfm:shortTermForecast:edit
* wfm:shortTermForecast:view
* wfm:timeOffLimit:add
* wfm:timeOffLimit:delete
* wfm:timeOffLimit:edit
* wfm:timeOffLimit:view
* wfm:timeOffPlan:add
* wfm:timeOffPlan:delete
* wfm:timeOffPlan:edit
* wfm:timeOffPlan:view
* wfm:timeOffRequest:add
* wfm:timeOffRequest:edit
* wfm:timeOffRequest:view
* wfm:workPlan:add
* wfm:workPlan:delete
* wfm:workPlan:edit
* wfm:workPlan:view
* wfm:workPlanRotation:add
* wfm:workPlanRotation:delete
* wfm:workPlanRotation:edit
* wfm:workPlanRotation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit, or 'mine' for the business unit of the logged-in user.
force_download_service = True # bool | Force the result of this operation to be sent via download service. For testing/app development purposes (optional)

try:
    # Get activity codes
    api_response = api_instance.get_workforcemanagement_businessunit_activitycodes(business_unit_id, force_download_service=force_download_service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_activitycodes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit, or &#39;mine&#39; for the business unit of the logged-in user. |  |
| **force_download_service** | **bool**| Force the result of this operation to be sent via download service. For testing/app development purposes | [optional]  |

### Return type

[**BusinessUnitActivityCodeListing**](BusinessUnitActivityCodeListing)


## get_workforcemanagement_businessunit_activityplan

> [**ActivityPlanResponse**](ActivityPlanResponse) get_workforcemanagement_businessunit_activityplan(business_unit_id, activity_plan_id)


Get an activity plan

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/activityplans/{activityPlanId} 

Requires ANY permissions: 

* wfm:activityPlan:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
activity_plan_id = 'activity_plan_id_example' # str | The ID of the activity plan to fetch

try:
    # Get an activity plan
    api_response = api_instance.get_workforcemanagement_businessunit_activityplan(business_unit_id, activity_plan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_activityplan: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **activity_plan_id** | **str**| The ID of the activity plan to fetch |  |

### Return type

[**ActivityPlanResponse**](ActivityPlanResponse)


## get_workforcemanagement_businessunit_activityplan_runs_job

> [**ActivityPlanRunJobResponse**](ActivityPlanRunJobResponse) get_workforcemanagement_businessunit_activityplan_runs_job(business_unit_id, activity_plan_id, job_id)


Gets an activity plan run job

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/activityplans/{activityPlanId}/runs/jobs/{jobId} 

Requires ANY permissions: 

* wfm:activityPlanRunJob:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
activity_plan_id = 'activity_plan_id_example' # str | The ID of the activity plan associated with the run job
job_id = 'job_id_example' # str | The ID of the activity plan run job

try:
    # Gets an activity plan run job
    api_response = api_instance.get_workforcemanagement_businessunit_activityplan_runs_job(business_unit_id, activity_plan_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_activityplan_runs_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **activity_plan_id** | **str**| The ID of the activity plan associated with the run job |  |
| **job_id** | **str**| The ID of the activity plan run job |  |

### Return type

[**ActivityPlanRunJobResponse**](ActivityPlanRunJobResponse)


## get_workforcemanagement_businessunit_activityplans

> [**ActivityPlanListing**](ActivityPlanListing) get_workforcemanagement_businessunit_activityplans(business_unit_id, state=state)


Get activity plans

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/activityplans 

Requires ANY permissions: 

* wfm:activityPlan:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
state = 'state_example' # str | Optionally filter by activity plan state (optional)

try:
    # Get activity plans
    api_response = api_instance.get_workforcemanagement_businessunit_activityplans(business_unit_id, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_activityplans: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **state** | **str**| Optionally filter by activity plan state | [optional] <br />**Values**: Active, Inactive |

### Return type

[**ActivityPlanListing**](ActivityPlanListing)


## get_workforcemanagement_businessunit_activityplans_jobs

> [**ActivityPlanJobListing**](ActivityPlanJobListing) get_workforcemanagement_businessunit_activityplans_jobs(business_unit_id)


Gets the latest job for all activity plans in the business unit

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/activityplans/jobs 

Requires ANY permissions: 

* wfm:activityPlan:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit

try:
    # Gets the latest job for all activity plans in the business unit
    api_response = api_instance.get_workforcemanagement_businessunit_activityplans_jobs(business_unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_activityplans_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |

### Return type

[**ActivityPlanJobListing**](ActivityPlanJobListing)


## get_workforcemanagement_businessunit_alternativeshifts_settings

> [**AlternativeShiftBuSettingsResponse**](AlternativeShiftBuSettingsResponse) get_workforcemanagement_businessunit_alternativeshifts_settings(business_unit_id)


Get alternative shifts settings for a business unit

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/alternativeshifts/settings 

Requires ANY permissions: 

* wfm:businessUnit:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit

try:
    # Get alternative shifts settings for a business unit
    api_response = api_instance.get_workforcemanagement_businessunit_alternativeshifts_settings(business_unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_alternativeshifts_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |

### Return type

[**AlternativeShiftBuSettingsResponse**](AlternativeShiftBuSettingsResponse)


## get_workforcemanagement_businessunit_alternativeshifts_trade

> [**AlternativeShiftTradeResponse**](AlternativeShiftTradeResponse) get_workforcemanagement_businessunit_alternativeshifts_trade(business_unit_id, trade_id)


Get an alternative shifts trade in a business unit for a given trade ID

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/alternativeshifts/trades/{tradeId} 

Requires ANY permissions: 

* wfm:alternativeShift:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
trade_id = 'trade_id_example' # str | The ID of the alternative shift trade

try:
    # Get an alternative shifts trade in a business unit for a given trade ID
    api_response = api_instance.get_workforcemanagement_businessunit_alternativeshifts_trade(business_unit_id, trade_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_alternativeshifts_trade: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **trade_id** | **str**| The ID of the alternative shift trade |  |

### Return type

[**AlternativeShiftTradeResponse**](AlternativeShiftTradeResponse)


## get_workforcemanagement_businessunit_alternativeshifts_trades_search_job

> [**BuAlternativeShiftJobResponse**](BuAlternativeShiftJobResponse) get_workforcemanagement_businessunit_alternativeshifts_trades_search_job(business_unit_id, job_id)


Query the status of an alternative shift search trade operation. Only the user who started the operation can query the status

Job details are only retained if the initial request returned a 202 ACCEPTED response

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/alternativeshifts/trades/search/jobs/{jobId} 

Requires ANY permissions: 

* wfm:alternativeShift:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
job_id = 'job_id_example' # str | The ID of the job

try:
    # Query the status of an alternative shift search trade operation. Only the user who started the operation can query the status
    api_response = api_instance.get_workforcemanagement_businessunit_alternativeshifts_trades_search_job(business_unit_id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_alternativeshifts_trades_search_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **job_id** | **str**| The ID of the job |  |

### Return type

[**BuAlternativeShiftJobResponse**](BuAlternativeShiftJobResponse)


## get_workforcemanagement_businessunit_intraday_planninggroups

> [**WfmIntradayPlanningGroupListing**](WfmIntradayPlanningGroupListing) get_workforcemanagement_businessunit_intraday_planninggroups(business_unit_id, date)


Get intraday planning groups for the given date

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/intraday/planninggroups 

Requires ANY permissions: 

* wfm:intraday:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
date = '2013-10-20' # date | yyyy-MM-dd date string interpreted in the configured business unit time zone. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

try:
    # Get intraday planning groups for the given date
    api_response = api_instance.get_workforcemanagement_businessunit_intraday_planninggroups(business_unit_id, date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_intraday_planninggroups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **date** | **date**| yyyy-MM-dd date string interpreted in the configured business unit time zone. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |

### Return type

[**WfmIntradayPlanningGroupListing**](WfmIntradayPlanningGroupListing)


## get_workforcemanagement_businessunit_mainforecast_continuousforecast_session

> [**ContinuousForecastGetSessionResponse**](ContinuousForecastGetSessionResponse) get_workforcemanagement_businessunit_mainforecast_continuousforecast_session(business_unit_id)


Get the latest session for the business unit ID

get_workforcemanagement_businessunit_mainforecast_continuousforecast_session is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/mainforecast/continuousforecast/session 

Requires ALL permissions: 

* wfm:mainForecast:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | 

try:
    # Get the latest session for the business unit ID
    api_response = api_instance.get_workforcemanagement_businessunit_mainforecast_continuousforecast_session(business_unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_mainforecast_continuousforecast_session: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**|  |  |

### Return type

[**ContinuousForecastGetSessionResponse**](ContinuousForecastGetSessionResponse)


## get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id

> [**ContinuousForecastSessionResponse**](ContinuousForecastSessionResponse) get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id(business_unit_id, session_id)


Get the session details for the session ID

get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/mainforecast/continuousforecast/session/{sessionId} 

Requires ALL permissions: 

* wfm:mainForecast:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | 
session_id = 'session_id_example' # str | 

try:
    # Get the session details for the session ID
    api_response = api_instance.get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id(business_unit_id, session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**|  |  |
| **session_id** | **str**|  |  |

### Return type

[**ContinuousForecastSessionResponse**](ContinuousForecastSessionResponse)


## get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id_snapshot_snapshot_id

> [**ContinuousForecastSnapshotResponse**](ContinuousForecastSnapshotResponse) get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id_snapshot_snapshot_id(business_unit_id, session_id, snapshot_id)


Get the snapshot details for the snapshot ID

get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id_snapshot_snapshot_id is a preview method and is subject to both breaking and non-breaking changes at any time without notice

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/mainforecast/continuousforecast/session/{sessionId}/snapshot/{snapshotId} 

Requires ALL permissions: 

* wfm:mainForecast:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | 
session_id = 'session_id_example' # str | 
snapshot_id = 'snapshot_id_example' # str | 

try:
    # Get the snapshot details for the snapshot ID
    api_response = api_instance.get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id_snapshot_snapshot_id(business_unit_id, session_id, snapshot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_mainforecast_continuousforecast_session_session_id_snapshot_snapshot_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**|  |  |
| **session_id** | **str**|  |  |
| **snapshot_id** | **str**|  |  |

### Return type

[**ContinuousForecastSnapshotResponse**](ContinuousForecastSnapshotResponse)


## get_workforcemanagement_businessunit_managementunits

> [**ManagementUnitListing**](ManagementUnitListing) get_workforcemanagement_businessunit_managementunits(business_unit_id, feature=feature, division_id=division_id)


Get all authorized management units in the business unit

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/managementunits 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit, or 'mine' for the business unit of the logged-in user.
feature = 'feature_example' # str | If specified, the list of management units for which the user is authorized to use the requested feature will be returned (optional)
division_id = 'division_id_example' # str | If specified, the list of management units belonging to the specified division will be returned (optional)

try:
    # Get all authorized management units in the business unit
    api_response = api_instance.get_workforcemanagement_businessunit_managementunits(business_unit_id, feature=feature, division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_managementunits: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit, or &#39;mine&#39; for the business unit of the logged-in user. |  |
| **feature** | **str**| If specified, the list of management units for which the user is authorized to use the requested feature will be returned | [optional] <br />**Values**: AgentSchedule, AgentTimeOffRequest, AgentWorkPlanBid, AlternativeShift, Coaching, Learning, ActivityCodes, ActivityPlans, Agents, BuActivityCodes, BusinessUnits, CapacityPlan, ContinuousForecast, HistoricalAdherence, HistoricalShrinkage, IntradayMonitoring, BuIntradayMonitoring, ManagementUnits, RealTimeAdherence, Schedules, BuSchedules, ServiceGoalTemplates, PlanningGroups, LongTermStaffing, ShiftTrading, ShortTermForecasts, BuShortTermForecasts, StaffingGroups, TimeOffPlans, TimeOffRequests, TimeOffLimits, WorkPlanBids, WorkPlanBidGroups, WorkPlanRotations, WorkPlans |
| **division_id** | **str**| If specified, the list of management units belonging to the specified division will be returned | [optional]  |

### Return type

[**ManagementUnitListing**](ManagementUnitListing)


## get_workforcemanagement_businessunit_planninggroup

> [**PlanningGroup**](PlanningGroup) get_workforcemanagement_businessunit_planninggroup(business_unit_id, planning_group_id)


Get a planning group

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/planninggroups/{planningGroupId} 

Requires ANY permissions: 

* wfm:planningGroup:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit.
planning_group_id = 'planning_group_id_example' # str | The ID of a planning group to fetch

try:
    # Get a planning group
    api_response = api_instance.get_workforcemanagement_businessunit_planninggroup(business_unit_id, planning_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_planninggroup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit. |  |
| **planning_group_id** | **str**| The ID of a planning group to fetch |  |

### Return type

[**PlanningGroup**](PlanningGroup)


## get_workforcemanagement_businessunit_planninggroups

> [**PlanningGroupList**](PlanningGroupList) get_workforcemanagement_businessunit_planninggroups(business_unit_id)


Gets list of planning groups

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/planninggroups 

Requires ANY permissions: 

* wfm:planningGroup:view
* wfm:shortTermForecast:view
* wfm:intraday:view
* wfm:agent:view
* wfm:schedule:view
* wfm:publishedSchedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit.

try:
    # Gets list of planning groups
    api_response = api_instance.get_workforcemanagement_businessunit_planninggroups(business_unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_planninggroups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit. |  |

### Return type

[**PlanningGroupList**](PlanningGroupList)


## get_workforcemanagement_businessunit_scheduling_run

> [**BuScheduleRun**](BuScheduleRun) get_workforcemanagement_businessunit_scheduling_run(business_unit_id, run_id)


Get a scheduling run

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/scheduling/runs/{runId} 

Requires ANY permissions: 

* wfm:schedule:generate
* wfm:schedule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
run_id = 'run_id_example' # str | The ID of the schedule run

try:
    # Get a scheduling run
    api_response = api_instance.get_workforcemanagement_businessunit_scheduling_run(business_unit_id, run_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_scheduling_run: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **run_id** | **str**| The ID of the schedule run |  |

### Return type

[**BuScheduleRun**](BuScheduleRun)


## get_workforcemanagement_businessunit_scheduling_run_result

> [**BuRescheduleResult**](BuRescheduleResult) get_workforcemanagement_businessunit_scheduling_run_result(business_unit_id, run_id, management_unit_ids, expand)


Get the result of a rescheduling operation

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/scheduling/runs/{runId}/result 

Requires ANY permissions: 

* wfm:schedule:edit
* wfm:schedule:generate

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
run_id = 'run_id_example' # str | The ID of the schedule run
management_unit_ids = ['management_unit_ids_example'] # list[str] | The IDs of the management units for which to fetch the reschedule results
expand = ['expand_example'] # list[str] | The fields to expand. Omitting will return an empty response

try:
    # Get the result of a rescheduling operation
    api_response = api_instance.get_workforcemanagement_businessunit_scheduling_run_result(business_unit_id, run_id, management_unit_ids, expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_scheduling_run_result: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **run_id** | **str**| The ID of the schedule run |  |
| **management_unit_ids** | [**list[str]**](str)| The IDs of the management units for which to fetch the reschedule results |  |
| **expand** | [**list[str]**](str)| The fields to expand. Omitting will return an empty response | <br />**Values**: headcountForecast, generationResults, agentSchedules |

### Return type

[**BuRescheduleResult**](BuRescheduleResult)


## get_workforcemanagement_businessunit_scheduling_runs

> [**BuScheduleRunListing**](BuScheduleRunListing) get_workforcemanagement_businessunit_scheduling_runs(business_unit_id)


Get the list of scheduling runs

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/scheduling/runs 

Requires ANY permissions: 

* wfm:schedule:generate
* wfm:schedule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit

try:
    # Get the list of scheduling runs
    api_response = api_instance.get_workforcemanagement_businessunit_scheduling_runs(business_unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_scheduling_runs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |

### Return type

[**BuScheduleRunListing**](BuScheduleRunListing)


## get_workforcemanagement_businessunit_servicegoaltemplate

> [**ServiceGoalTemplate**](ServiceGoalTemplate) get_workforcemanagement_businessunit_servicegoaltemplate(business_unit_id, service_goal_template_id, expand=expand)


Get a service goal template

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/servicegoaltemplates/{serviceGoalTemplateId} 

Requires ANY permissions: 

* wfm:serviceGoalTemplate:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit.
service_goal_template_id = 'service_goal_template_id_example' # str | The ID of a service goal template to fetch
expand = ['expand_example'] # list[str] | Include to access additional data on the service goal template (optional)

try:
    # Get a service goal template
    api_response = api_instance.get_workforcemanagement_businessunit_servicegoaltemplate(business_unit_id, service_goal_template_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_servicegoaltemplate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit. |  |
| **service_goal_template_id** | **str**| The ID of a service goal template to fetch |  |
| **expand** | [**list[str]**](str)| Include to access additional data on the service goal template | [optional] <br />**Values**: impactOverride |

### Return type

[**ServiceGoalTemplate**](ServiceGoalTemplate)


## get_workforcemanagement_businessunit_servicegoaltemplates

> [**ServiceGoalTemplateList**](ServiceGoalTemplateList) get_workforcemanagement_businessunit_servicegoaltemplates(business_unit_id, expand=expand)


Gets list of service goal templates

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/servicegoaltemplates 

Requires ANY permissions: 

* wfm:serviceGoalTemplate:view
* wfm:planningGroup:view
* wfm:shortTermForecast:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit.
expand = ['expand_example'] # list[str] | Include to access additional data on the service goal template (optional)

try:
    # Gets list of service goal templates
    api_response = api_instance.get_workforcemanagement_businessunit_servicegoaltemplates(business_unit_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_servicegoaltemplates: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit. |  |
| **expand** | [**list[str]**](str)| Include to access additional data on the service goal template | [optional] <br />**Values**: impactOverride |

### Return type

[**ServiceGoalTemplateList**](ServiceGoalTemplateList)


## get_workforcemanagement_businessunit_staffinggroup

> [**StaffingGroupResponse**](StaffingGroupResponse) get_workforcemanagement_businessunit_staffinggroup(business_unit_id, staffing_group_id)


Gets a staffing group

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/staffinggroups/{staffingGroupId} 

Requires ANY permissions: 

* wfm:staffingGroup:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
staffing_group_id = 'staffing_group_id_example' # str | The ID of the staffing group to fetch

try:
    # Gets a staffing group
    api_response = api_instance.get_workforcemanagement_businessunit_staffinggroup(business_unit_id, staffing_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_staffinggroup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **staffing_group_id** | **str**| The ID of the staffing group to fetch |  |

### Return type

[**StaffingGroupResponse**](StaffingGroupResponse)


## get_workforcemanagement_businessunit_staffinggroups

> [**StaffingGroupListing**](StaffingGroupListing) get_workforcemanagement_businessunit_staffinggroups(business_unit_id, management_unit_id=management_unit_id)


Gets a list of staffing groups

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/staffinggroups 

Requires ANY permissions: 

* wfm:staffingGroup:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit to get management unit specific staffing groups (optional)

try:
    # Gets a list of staffing groups
    api_response = api_instance.get_workforcemanagement_businessunit_staffinggroups(business_unit_id, management_unit_id=management_unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_staffinggroups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **management_unit_id** | **str**| The ID of the management unit to get management unit specific staffing groups | [optional]  |

### Return type

[**StaffingGroupListing**](StaffingGroupListing)


## get_workforcemanagement_businessunit_timeofflimit

> [**BuTimeOffLimitResponse**](BuTimeOffLimitResponse) get_workforcemanagement_businessunit_timeofflimit(business_unit_id, time_off_limit_id)


Gets a time-off limit object

Returns properties of time-off limit object, but not daily values

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/timeofflimits/{timeOffLimitId} 

Requires ANY permissions: 

* wfm:timeOffLimit:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
time_off_limit_id = 'time_off_limit_id_example' # str | The ID of the time-off limit to fetch

try:
    # Gets a time-off limit object
    api_response = api_instance.get_workforcemanagement_businessunit_timeofflimit(business_unit_id, time_off_limit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_timeofflimit: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **time_off_limit_id** | **str**| The ID of the time-off limit to fetch |  |

### Return type

[**BuTimeOffLimitResponse**](BuTimeOffLimitResponse)


## get_workforcemanagement_businessunit_timeofflimits

> [**BuTimeOffLimitListing**](BuTimeOffLimitListing) get_workforcemanagement_businessunit_timeofflimits(business_unit_id, management_unit_id=management_unit_id)


Gets a list of time-off limit objects

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/timeofflimits 

Requires ANY permissions: 

* wfm:timeOffLimit:view
* wfm:timeOffPlan:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit to get management unit specific time-off limit objects (optional)

try:
    # Gets a list of time-off limit objects
    api_response = api_instance.get_workforcemanagement_businessunit_timeofflimits(business_unit_id, management_unit_id=management_unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_timeofflimits: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **management_unit_id** | **str**| The ID of the management unit to get management unit specific time-off limit objects | [optional]  |

### Return type

[**BuTimeOffLimitListing**](BuTimeOffLimitListing)


## get_workforcemanagement_businessunit_timeoffplan

> [**BuTimeOffPlanResponse**](BuTimeOffPlanResponse) get_workforcemanagement_businessunit_timeoffplan(business_unit_id, time_off_plan_id)


Gets a time-off plan

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/timeoffplans/{timeOffPlanId} 

Requires ANY permissions: 

* wfm:timeOffPlan:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
time_off_plan_id = 'time_off_plan_id_example' # str | The ID of the time-off plan to fetch

try:
    # Gets a time-off plan
    api_response = api_instance.get_workforcemanagement_businessunit_timeoffplan(business_unit_id, time_off_plan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_timeoffplan: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **time_off_plan_id** | **str**| The ID of the time-off plan to fetch |  |

### Return type

[**BuTimeOffPlanResponse**](BuTimeOffPlanResponse)


## get_workforcemanagement_businessunit_timeoffplans

> [**BuTimeOffPlanListing**](BuTimeOffPlanListing) get_workforcemanagement_businessunit_timeoffplans(business_unit_id, management_unit_id=management_unit_id, force_download_service=force_download_service)


Gets a list of time-off plans

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/timeoffplans 

Requires ANY permissions: 

* wfm:timeOffPlan:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit to get management unit specific staffing groups (optional)
force_download_service = True # bool | Force the result of this operation to be sent via download service. For testing/app development purposes (optional)

try:
    # Gets a list of time-off plans
    api_response = api_instance.get_workforcemanagement_businessunit_timeoffplans(business_unit_id, management_unit_id=management_unit_id, force_download_service=force_download_service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_timeoffplans: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **management_unit_id** | **str**| The ID of the management unit to get management unit specific staffing groups | [optional]  |
| **force_download_service** | **bool**| Force the result of this operation to be sent via download service. For testing/app development purposes | [optional]  |

### Return type

[**BuTimeOffPlanListing**](BuTimeOffPlanListing)


## get_workforcemanagement_businessunit_week_schedule

> [**BuScheduleMetadata**](BuScheduleMetadata) get_workforcemanagement_businessunit_week_schedule(business_unit_id, week_id, schedule_id, expand=expand)


Get the metadata for the schedule, describing which management units and agents are in the scheduleSchedule data can then be loaded with the query route

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId} 

Requires ANY permissions: 

* wfm:schedule:view
* wfm:publishedSchedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
week_id = '2013-10-20' # date | First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
schedule_id = 'schedule_id_example' # str | The ID of the schedule
expand = 'expand_example' # str | expand (optional)

try:
    # Get the metadata for the schedule, describing which management units and agents are in the scheduleSchedule data can then be loaded with the query route
    api_response = api_instance.get_workforcemanagement_businessunit_week_schedule(business_unit_id, week_id, schedule_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_week_schedule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **week_id** | **date**| First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **schedule_id** | **str**| The ID of the schedule |  |
| **expand** | **str**| expand | [optional] <br />**Values**: managementUnits.agents |

### Return type

[**BuScheduleMetadata**](BuScheduleMetadata)


## get_workforcemanagement_businessunit_week_schedule_generationresults

> [**ScheduleGenerationResult**](ScheduleGenerationResult) get_workforcemanagement_businessunit_week_schedule_generationresults(business_unit_id, week_id, schedule_id)


Get the generation results for a generated schedule

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId}/generationresults 

Requires ANY permissions: 

* wfm:schedule:view
* wfm:publishedSchedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
week_id = '2013-10-20' # date | First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
schedule_id = 'schedule_id_example' # str | The ID of the schedule

try:
    # Get the generation results for a generated schedule
    api_response = api_instance.get_workforcemanagement_businessunit_week_schedule_generationresults(business_unit_id, week_id, schedule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_week_schedule_generationresults: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **week_id** | **date**| First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **schedule_id** | **str**| The ID of the schedule |  |

### Return type

[**ScheduleGenerationResult**](ScheduleGenerationResult)


## get_workforcemanagement_businessunit_week_schedule_headcountforecast

> [**BuHeadcountForecastResponse**](BuHeadcountForecastResponse) get_workforcemanagement_businessunit_week_schedule_headcountforecast(business_unit_id, week_id, schedule_id, force_download=force_download)


Get the headcount forecast by planning group for the schedule

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId}/headcountforecast 

Requires ANY permissions: 

* wfm:schedule:view
* wfm:publishedSchedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
week_id = '2013-10-20' # date | First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
schedule_id = 'schedule_id_example' # str | The ID of the schedule
force_download = True # bool | Whether to force the result to come via download url.  For testing purposes only (optional)

try:
    # Get the headcount forecast by planning group for the schedule
    api_response = api_instance.get_workforcemanagement_businessunit_week_schedule_headcountforecast(business_unit_id, week_id, schedule_id, force_download=force_download)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_week_schedule_headcountforecast: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **week_id** | **date**| First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **schedule_id** | **str**| The ID of the schedule |  |
| **force_download** | **bool**| Whether to force the result to come via download url.  For testing purposes only | [optional]  |

### Return type

[**BuHeadcountForecastResponse**](BuHeadcountForecastResponse)


## get_workforcemanagement_businessunit_week_schedule_history_agent

> [**BuAgentScheduleHistoryResponse**](BuAgentScheduleHistoryResponse) get_workforcemanagement_businessunit_week_schedule_history_agent(business_unit_id, week_id, schedule_id, agent_id)


Loads agent's schedule history.

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId}/history/agents/{agentId} 

Requires ANY permissions: 

* wfm:schedule:view
* wfm:publishedSchedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
week_id = '2013-10-20' # date | First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
schedule_id = 'schedule_id_example' # str | The ID of the schedule
agent_id = 'agent_id_example' # str | THe ID of the agent

try:
    # Loads agent's schedule history.
    api_response = api_instance.get_workforcemanagement_businessunit_week_schedule_history_agent(business_unit_id, week_id, schedule_id, agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_week_schedule_history_agent: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **week_id** | **date**| First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **schedule_id** | **str**| The ID of the schedule |  |
| **agent_id** | **str**| THe ID of the agent |  |

### Return type

[**BuAgentScheduleHistoryResponse**](BuAgentScheduleHistoryResponse)


## get_workforcemanagement_businessunit_week_schedule_performancepredictions

> [**PerformancePredictionResponse**](PerformancePredictionResponse) get_workforcemanagement_businessunit_week_schedule_performancepredictions(business_unit_id, week_id, schedule_id)


Get the performance prediction for the associated schedule

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId}/performancepredictions 

Requires ANY permissions: 

* wfm:schedule:view
* wfm:publishedSchedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit to which the performance prediction belongs
week_id = 'week_id_example' # str | First day of schedule week in yyyy-MM-dd format
schedule_id = 'schedule_id_example' # str | The ID of the schedule the performance prediction belongs to

try:
    # Get the performance prediction for the associated schedule
    api_response = api_instance.get_workforcemanagement_businessunit_week_schedule_performancepredictions(business_unit_id, week_id, schedule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_week_schedule_performancepredictions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit to which the performance prediction belongs |  |
| **week_id** | **str**| First day of schedule week in yyyy-MM-dd format |  |
| **schedule_id** | **str**| The ID of the schedule the performance prediction belongs to |  |

### Return type

[**PerformancePredictionResponse**](PerformancePredictionResponse)


## get_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculation

> [**PerformancePredictionRecalculationResponse**](PerformancePredictionRecalculationResponse) get_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculation(business_unit_id, week_id, schedule_id, recalculation_id)


Get recalculated performance prediction result

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId}/performancepredictions/recalculations/{recalculationId} 

Requires ANY permissions: 

* wfm:schedule:view
* wfm:publishedSchedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit to which the performance prediction belongs
week_id = 'week_id_example' # str | First day of schedule week in yyyy-MM-dd format
schedule_id = 'schedule_id_example' # str | The ID of the schedule the recalculation belongs to
recalculation_id = 'recalculation_id_example' # str | The ID of the recalculation request

try:
    # Get recalculated performance prediction result
    api_response = api_instance.get_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculation(business_unit_id, week_id, schedule_id, recalculation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit to which the performance prediction belongs |  |
| **week_id** | **str**| First day of schedule week in yyyy-MM-dd format |  |
| **schedule_id** | **str**| The ID of the schedule the recalculation belongs to |  |
| **recalculation_id** | **str**| The ID of the recalculation request |  |

### Return type

[**PerformancePredictionRecalculationResponse**](PerformancePredictionRecalculationResponse)


## get_workforcemanagement_businessunit_week_schedules

> [**BuScheduleListing**](BuScheduleListing) get_workforcemanagement_businessunit_week_schedules(business_unit_id, week_id, include_only_published=include_only_published, expand=expand)


Get the list of week schedules for the specified week

Use \"recent\" (without quotes) for the `weekId` path parameter to fetch all forecasts for +/- 26 weeks from the current date. Response will include any schedule which spans the specified week

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules 

Requires ANY permissions: 

* wfm:schedule:view
* wfm:publishedSchedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
week_id = 'week_id_example' # str | First day of schedule week in yyyy-MM-dd format, or 'recent' (without quotes) to get recent schedules
include_only_published = True # bool | includeOnlyPublished (optional)
expand = 'expand_example' # str | expand (optional)

try:
    # Get the list of week schedules for the specified week
    api_response = api_instance.get_workforcemanagement_businessunit_week_schedules(business_unit_id, week_id, include_only_published=include_only_published, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_week_schedules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **week_id** | **str**| First day of schedule week in yyyy-MM-dd format, or &#39;recent&#39; (without quotes) to get recent schedules |  |
| **include_only_published** | **bool**| includeOnlyPublished | [optional]  |
| **expand** | **str**| expand | [optional] <br />**Values**: forecast.description |

### Return type

[**BuScheduleListing**](BuScheduleListing)


## get_workforcemanagement_businessunit_week_shorttermforecast

> [**BuShortTermForecast**](BuShortTermForecast) get_workforcemanagement_businessunit_week_shorttermforecast(business_unit_id, week_date_id, forecast_id, expand=expand)


Get a short term forecast

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekDateId}/shorttermforecasts/{forecastId} 

Requires ANY permissions: 

* wfm:shortTermForecast:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit to which the forecast belongs
week_date_id = '2013-10-20' # date | The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
forecast_id = 'forecast_id_example' # str | The ID of the forecast
expand = ['expand_example'] # list[str] | Include to access additional data on the forecast (optional)

try:
    # Get a short term forecast
    api_response = api_instance.get_workforcemanagement_businessunit_week_shorttermforecast(business_unit_id, week_date_id, forecast_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_week_shorttermforecast: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit to which the forecast belongs |  |
| **week_date_id** | **date**| The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **forecast_id** | **str**| The ID of the forecast |  |
| **expand** | [**list[str]**](str)| Include to access additional data on the forecast | [optional] <br />**Values**: planningGroups, generationResults |

### Return type

[**BuShortTermForecast**](BuShortTermForecast)


## get_workforcemanagement_businessunit_week_shorttermforecast_data

> [**BuForecastResultResponse**](BuForecastResultResponse) get_workforcemanagement_businessunit_week_shorttermforecast_data(business_unit_id, week_date_id, forecast_id, week_number=week_number, force_download_service=force_download_service)


Get the result of a short term forecast calculation

Includes modifications unless you pass the doNotApplyModifications query parameter

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekDateId}/shorttermforecasts/{forecastId}/data 

Requires ANY permissions: 

* wfm:shortTermForecast:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit to which the forecast belongs
week_date_id = '2013-10-20' # date | The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
forecast_id = 'forecast_id_example' # str | The ID of the forecast
week_number = 56 # int | The week number to fetch (for multi-week forecasts) (optional)
force_download_service = True # bool | Force the result of this operation to be sent via download service.  For testing/app development purposes (optional)

try:
    # Get the result of a short term forecast calculation
    api_response = api_instance.get_workforcemanagement_businessunit_week_shorttermforecast_data(business_unit_id, week_date_id, forecast_id, week_number=week_number, force_download_service=force_download_service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_week_shorttermforecast_data: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit to which the forecast belongs |  |
| **week_date_id** | **date**| The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **forecast_id** | **str**| The ID of the forecast |  |
| **week_number** | **int**| The week number to fetch (for multi-week forecasts) | [optional]  |
| **force_download_service** | **bool**| Force the result of this operation to be sent via download service.  For testing/app development purposes | [optional]  |

### Return type

[**BuForecastResultResponse**](BuForecastResultResponse)


## get_workforcemanagement_businessunit_week_shorttermforecast_generationresults

> [**BuForecastGenerationResult**](BuForecastGenerationResult) get_workforcemanagement_businessunit_week_shorttermforecast_generationresults(business_unit_id, week_date_id, forecast_id)


Gets the forecast generation results

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekDateId}/shorttermforecasts/{forecastId}/generationresults 

Requires ANY permissions: 

* wfm:shortTermForecast:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit to which the forecast belongs
week_date_id = '2013-10-20' # date | The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
forecast_id = 'forecast_id_example' # str | The ID of the forecast

try:
    # Gets the forecast generation results
    api_response = api_instance.get_workforcemanagement_businessunit_week_shorttermforecast_generationresults(business_unit_id, week_date_id, forecast_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_week_shorttermforecast_generationresults: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit to which the forecast belongs |  |
| **week_date_id** | **date**| The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **forecast_id** | **str**| The ID of the forecast |  |

### Return type

[**BuForecastGenerationResult**](BuForecastGenerationResult)


## get_workforcemanagement_businessunit_week_shorttermforecast_longtermforecastdata

> [**LongTermForecastResultResponse**](LongTermForecastResultResponse) get_workforcemanagement_businessunit_week_shorttermforecast_longtermforecastdata(business_unit_id, week_date_id, forecast_id, force_download_service=force_download_service)


Get the result of a long term forecast calculation

Includes modifications unless you pass the doNotApplyModifications query parameter

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekDateId}/shorttermforecasts/{forecastId}/longtermforecastdata 

Requires ANY permissions: 

* wfm:shortTermForecast:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit to which the forecast belongs
week_date_id = '2013-10-20' # date | The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
forecast_id = 'forecast_id_example' # str | The ID of the forecast
force_download_service = True # bool | Force the result of this operation to be sent via download service.  For testing/app development purposes (optional)

try:
    # Get the result of a long term forecast calculation
    api_response = api_instance.get_workforcemanagement_businessunit_week_shorttermforecast_longtermforecastdata(business_unit_id, week_date_id, forecast_id, force_download_service=force_download_service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_week_shorttermforecast_longtermforecastdata: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit to which the forecast belongs |  |
| **week_date_id** | **date**| The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **forecast_id** | **str**| The ID of the forecast |  |
| **force_download_service** | **bool**| Force the result of this operation to be sent via download service.  For testing/app development purposes | [optional]  |

### Return type

[**LongTermForecastResultResponse**](LongTermForecastResultResponse)


## get_workforcemanagement_businessunit_week_shorttermforecast_planninggroups

> [**ForecastPlanningGroupsResponse**](ForecastPlanningGroupsResponse) get_workforcemanagement_businessunit_week_shorttermforecast_planninggroups(business_unit_id, week_date_id, forecast_id)


Gets the forecast planning group snapshot

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekDateId}/shorttermforecasts/{forecastId}/planninggroups 

Requires ANY permissions: 

* wfm:shortTermForecast:view
* wfm:schedule:view
* wfm:publishedSchedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit to which the forecast belongs
week_date_id = '2013-10-20' # date | The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
forecast_id = 'forecast_id_example' # str | The ID of the forecast

try:
    # Gets the forecast planning group snapshot
    api_response = api_instance.get_workforcemanagement_businessunit_week_shorttermforecast_planninggroups(business_unit_id, week_date_id, forecast_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_week_shorttermforecast_planninggroups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit to which the forecast belongs |  |
| **week_date_id** | **date**| The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **forecast_id** | **str**| The ID of the forecast |  |

### Return type

[**ForecastPlanningGroupsResponse**](ForecastPlanningGroupsResponse)


## get_workforcemanagement_businessunit_week_shorttermforecast_staffingrequirement

> [**BuForecastStaffingRequirementsResultResponse**](BuForecastStaffingRequirementsResultResponse) get_workforcemanagement_businessunit_week_shorttermforecast_staffingrequirement(business_unit_id, week_date_id, forecast_id, week_numbers=week_numbers)


Get the staffing requirement by planning group for a forecast

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekDateId}/shorttermforecasts/{forecastId}/staffingrequirement 

Requires ANY permissions: 

* wfm:staffingRequirement:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit to which the forecast belongs
week_date_id = '2013-10-20' # date | The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
forecast_id = 'forecast_id_example' # str | The ID of the forecast
week_numbers = ['week_numbers_example'] # list[str] | The week numbers to fetch (for multi-week forecasts) staffing requirements. Returns all week data if the list is not specified (optional)

try:
    # Get the staffing requirement by planning group for a forecast
    api_response = api_instance.get_workforcemanagement_businessunit_week_shorttermforecast_staffingrequirement(business_unit_id, week_date_id, forecast_id, week_numbers=week_numbers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_week_shorttermforecast_staffingrequirement: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit to which the forecast belongs |  |
| **week_date_id** | **date**| The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **forecast_id** | **str**| The ID of the forecast |  |
| **week_numbers** | [**list[str]**](str)| The week numbers to fetch (for multi-week forecasts) staffing requirements. Returns all week data if the list is not specified | [optional]  |

### Return type

[**BuForecastStaffingRequirementsResultResponse**](BuForecastStaffingRequirementsResultResponse)


## get_workforcemanagement_businessunit_week_shorttermforecasts

> [**BuShortTermForecastListing**](BuShortTermForecastListing) get_workforcemanagement_businessunit_week_shorttermforecasts(business_unit_id, week_date_id)


Get short term forecasts

Use \"recent\" (without quotes) for the `weekDateId` path parameter to fetch all forecasts for +/- 26 weeks from the current date. Response will include any forecast which spans the specified week

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekDateId}/shorttermforecasts 

Requires ANY permissions: 

* wfm:schedule:generate
* wfm:shortTermForecast:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit to which the forecast belongs
week_date_id = 'week_date_id_example' # str | The week start date of the forecast in yyyy-MM-dd format or 'recent' (without quotes) to fetch recent forecasts

try:
    # Get short term forecasts
    api_response = api_instance.get_workforcemanagement_businessunit_week_shorttermforecasts(business_unit_id, week_date_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_week_shorttermforecasts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit to which the forecast belongs |  |
| **week_date_id** | **str**| The week start date of the forecast in yyyy-MM-dd format or &#39;recent&#39; (without quotes) to fetch recent forecasts |  |

### Return type

[**BuShortTermForecastListing**](BuShortTermForecastListing)


## get_workforcemanagement_businessunit_workplanbid

> [**WorkPlanBid**](WorkPlanBid) get_workforcemanagement_businessunit_workplanbid(business_unit_id, bid_id)


Get a work plan bid

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/workplanbids/{bidId} 

Requires ANY permissions: 

* wfm:workPlanBid:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
bid_id = 'bid_id_example' # str | The id of the workplanbid

try:
    # Get a work plan bid
    api_response = api_instance.get_workforcemanagement_businessunit_workplanbid(business_unit_id, bid_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_workplanbid: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **bid_id** | **str**| The id of the workplanbid |  |

### Return type

[**WorkPlanBid**](WorkPlanBid)


## get_workforcemanagement_businessunit_workplanbid_group

> [**WorkPlanBidGroupResponse**](WorkPlanBidGroupResponse) get_workforcemanagement_businessunit_workplanbid_group(business_unit_id, bid_id, bid_group_id)


Get a bid group by bid group Id

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/workplanbids/{bidId}/groups/{bidGroupId} 

Requires ANY permissions: 

* wfm:workPlanBidGroup:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
bid_id = 'bid_id_example' # str | The work plan bid id of the bid groups
bid_group_id = 'bid_group_id_example' # str | Work Plan Bid Group id

try:
    # Get a bid group by bid group Id
    api_response = api_instance.get_workforcemanagement_businessunit_workplanbid_group(business_unit_id, bid_id, bid_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_workplanbid_group: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **bid_id** | **str**| The work plan bid id of the bid groups |  |
| **bid_group_id** | **str**| Work Plan Bid Group id |  |

### Return type

[**WorkPlanBidGroupResponse**](WorkPlanBidGroupResponse)


## get_workforcemanagement_businessunit_workplanbid_group_preferences

> [**AdminAgentWorkPlanPreferenceResponse**](AdminAgentWorkPlanPreferenceResponse) get_workforcemanagement_businessunit_workplanbid_group_preferences(business_unit_id, bid_id, bid_group_id)


Gets the work plan preferences of all the agents in the work plan bid group

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/workplanbids/{bidId}/groups/{bidGroupId}/preferences 

Requires ANY permissions: 

* wfm:workPlanBidGroup:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
bid_id = 'bid_id_example' # str | The work plan bid id of the bid groups
bid_group_id = 'bid_group_id_example' # str | The ID of the work plan bid group

try:
    # Gets the work plan preferences of all the agents in the work plan bid group
    api_response = api_instance.get_workforcemanagement_businessunit_workplanbid_group_preferences(business_unit_id, bid_id, bid_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_workplanbid_group_preferences: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **bid_id** | **str**| The work plan bid id of the bid groups |  |
| **bid_group_id** | **str**| The ID of the work plan bid group |  |

### Return type

[**AdminAgentWorkPlanPreferenceResponse**](AdminAgentWorkPlanPreferenceResponse)


## get_workforcemanagement_businessunit_workplanbid_groups_summary

> [**WorkPlanBidGroupSummaryList**](WorkPlanBidGroupSummaryList) get_workforcemanagement_businessunit_workplanbid_groups_summary(business_unit_id, bid_id)


Get summary of bid groups that belong to a work plan bid

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/workplanbids/{bidId}/groups/summary 

Requires ANY permissions: 

* wfm:workPlanBidGroup:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
bid_id = 'bid_id_example' # str | The work plan bid id of the bid groups

try:
    # Get summary of bid groups that belong to a work plan bid
    api_response = api_instance.get_workforcemanagement_businessunit_workplanbid_groups_summary(business_unit_id, bid_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_workplanbid_groups_summary: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **bid_id** | **str**| The work plan bid id of the bid groups |  |

### Return type

[**WorkPlanBidGroupSummaryList**](WorkPlanBidGroupSummaryList)


## get_workforcemanagement_businessunit_workplanbids

> [**WorkPlanBidListResponse**](WorkPlanBidListResponse) get_workforcemanagement_businessunit_workplanbids(business_unit_id)


Get list of work plan bids

Wraps GET /api/v2/workforcemanagement/businessunits/{businessUnitId}/workplanbids 

Requires ANY permissions: 

* wfm:workPlanBid:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit

try:
    # Get list of work plan bids
    api_response = api_instance.get_workforcemanagement_businessunit_workplanbids(business_unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunit_workplanbids: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |

### Return type

[**WorkPlanBidListResponse**](WorkPlanBidListResponse)


## get_workforcemanagement_businessunits

> [**BusinessUnitListing**](BusinessUnitListing) get_workforcemanagement_businessunits(feature=feature, division_id=division_id)


Get business units

Wraps GET /api/v2/workforcemanagement/businessunits 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
feature = 'feature_example' # str | If specified, the list of business units for which the user is authorized to use the requested feature will be returned (optional)
division_id = 'division_id_example' # str | If specified, the list of business units belonging to the specified division will be returned (optional)

try:
    # Get business units
    api_response = api_instance.get_workforcemanagement_businessunits(feature=feature, division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunits: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **feature** | **str**| If specified, the list of business units for which the user is authorized to use the requested feature will be returned | [optional] <br />**Values**: AgentSchedule, AgentTimeOffRequest, AgentWorkPlanBid, AlternativeShift, Coaching, Learning, ActivityCodes, ActivityPlans, Agents, BuActivityCodes, BusinessUnits, CapacityPlan, ContinuousForecast, HistoricalAdherence, HistoricalShrinkage, IntradayMonitoring, BuIntradayMonitoring, ManagementUnits, RealTimeAdherence, Schedules, BuSchedules, ServiceGoalTemplates, PlanningGroups, LongTermStaffing, ShiftTrading, ShortTermForecasts, BuShortTermForecasts, StaffingGroups, TimeOffPlans, TimeOffRequests, TimeOffLimits, WorkPlanBids, WorkPlanBidGroups, WorkPlanRotations, WorkPlans |
| **division_id** | **str**| If specified, the list of business units belonging to the specified division will be returned | [optional]  |

### Return type

[**BusinessUnitListing**](BusinessUnitListing)


## get_workforcemanagement_businessunits_divisionviews

> [**BusinessUnitListing**](BusinessUnitListing) get_workforcemanagement_businessunits_divisionviews(division_id=division_id)


Get business units across divisions

Wraps GET /api/v2/workforcemanagement/businessunits/divisionviews 

Requires ANY permissions: 

* wfm:businessUnit:search

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
division_id = ['division_id_example'] # list[str] | The divisionIds to filter by. If omitted, will return business units in all divisions (optional)

try:
    # Get business units across divisions
    api_response = api_instance.get_workforcemanagement_businessunits_divisionviews(division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_businessunits_divisionviews: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **division_id** | [**list[str]**](str)| The divisionIds to filter by. If omitted, will return business units in all divisions | [optional]  |

### Return type

[**BusinessUnitListing**](BusinessUnitListing)


## get_workforcemanagement_calendar_data_ics

> str** get_workforcemanagement_calendar_data_ics(calendar_id)


Get ics formatted calendar based on shareable link

Wraps GET /api/v2/workforcemanagement/calendar/data/ics 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
calendar_id = 'calendar_id_example' # str | The id of the ics-formatted calendar

try:
    # Get ics formatted calendar based on shareable link
    api_response = api_instance.get_workforcemanagement_calendar_data_ics(calendar_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_calendar_data_ics: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **calendar_id** | **str**| The id of the ics-formatted calendar |  |

### Return type

**str**


## get_workforcemanagement_calendar_url_ics

> [**CalendarUrlResponse**](CalendarUrlResponse) get_workforcemanagement_calendar_url_ics()


Get existing calendar link for the current user

Wraps GET /api/v2/workforcemanagement/calendar/url/ics 

Requires ALL permissions: 

* wfm:agentSchedule:sync
* wfm:agentSchedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()

try:
    # Get existing calendar link for the current user
    api_response = api_instance.get_workforcemanagement_calendar_url_ics()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_calendar_url_ics: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**CalendarUrlResponse**](CalendarUrlResponse)


## get_workforcemanagement_historicaldata_bulk_remove_job

> [**HistoricalImportDeleteFilesJobResponse**](HistoricalImportDeleteFilesJobResponse) get_workforcemanagement_historicaldata_bulk_remove_job(job_id)


Retrieves delete job status for historical data imports associated with the job id

Wraps GET /api/v2/workforcemanagement/historicaldata/bulk/remove/jobs/{jobId} 

Requires ALL permissions: 

* wfm:historicalData:upload

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
job_id = 'job_id_example' # str | The job ID of the historical data delete request

try:
    # Retrieves delete job status for historical data imports associated with the job id
    api_response = api_instance.get_workforcemanagement_historicaldata_bulk_remove_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_historicaldata_bulk_remove_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| The job ID of the historical data delete request |  |

### Return type

[**HistoricalImportDeleteFilesJobResponse**](HistoricalImportDeleteFilesJobResponse)


## get_workforcemanagement_historicaldata_bulk_remove_jobs

> [**HistoricalImportOverallDeleteStatusResponse**](HistoricalImportOverallDeleteStatusResponse) get_workforcemanagement_historicaldata_bulk_remove_jobs()


Retrieves all delete job status for historical data

Wraps GET /api/v2/workforcemanagement/historicaldata/bulk/remove/jobs 

Requires ALL permissions: 

* wfm:historicalData:upload

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()

try:
    # Retrieves all delete job status for historical data
    api_response = api_instance.get_workforcemanagement_historicaldata_bulk_remove_jobs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_historicaldata_bulk_remove_jobs: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**HistoricalImportOverallDeleteStatusResponse**](HistoricalImportOverallDeleteStatusResponse)


## get_workforcemanagement_historicaldata_deletejob

> [**HistoricalImportDeleteJobResponse**](HistoricalImportDeleteJobResponse) get_workforcemanagement_historicaldata_deletejob()

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Retrieves delete job status for historical data imports of the organization.

Deprecated: Please use GET /workforcemanagement/historicaldata/bulk/remove/jobs instead.

Wraps GET /api/v2/workforcemanagement/historicaldata/deletejob 

Requires ALL permissions: 

* wfm:historicalData:upload

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()

try:
    # Retrieves delete job status for historical data imports of the organization.
    api_response = api_instance.get_workforcemanagement_historicaldata_deletejob()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_historicaldata_deletejob: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**HistoricalImportDeleteJobResponse**](HistoricalImportDeleteJobResponse)


## get_workforcemanagement_historicaldata_importstatus

> [**HistoricalImportStatusListing**](HistoricalImportStatusListing) get_workforcemanagement_historicaldata_importstatus()


Retrieves status of the historical data imports of the organization

Wraps GET /api/v2/workforcemanagement/historicaldata/importstatus 

Requires ALL permissions: 

* wfm:historicalData:upload

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()

try:
    # Retrieves status of the historical data imports of the organization
    api_response = api_instance.get_workforcemanagement_historicaldata_importstatus()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_historicaldata_importstatus: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**HistoricalImportStatusListing**](HistoricalImportStatusListing)


## get_workforcemanagement_historicaldata_importstatus_job_id

> [**HistoricalImportStatusJobResponse**](HistoricalImportStatusJobResponse) get_workforcemanagement_historicaldata_importstatus_job_id(job_id)


Retrieves status of the historical data imports associated with job id

Wraps GET /api/v2/workforcemanagement/historicaldata/importstatus/{jobId} 

Requires ALL permissions: 

* wfm:historicalData:upload

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
job_id = 'job_id_example' # str | The job Id of the historical data import request

try:
    # Retrieves status of the historical data imports associated with job id
    api_response = api_instance.get_workforcemanagement_historicaldata_importstatus_job_id(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_historicaldata_importstatus_job_id: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| The job Id of the historical data import request |  |

### Return type

[**HistoricalImportStatusJobResponse**](HistoricalImportStatusJobResponse)


## get_workforcemanagement_integrations_hris

> [**WfmIntegrationListing**](WfmIntegrationListing) get_workforcemanagement_integrations_hris()


Get integrations

Wraps GET /api/v2/workforcemanagement/integrations/hris 

Requires ANY permissions: 

* wfm:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()

try:
    # Get integrations
    api_response = api_instance.get_workforcemanagement_integrations_hris()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_integrations_hris: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**WfmIntegrationListing**](WfmIntegrationListing)


## get_workforcemanagement_integrations_hris_timeofftypes_job

> [**HrisTimeOffTypesJobResponse**](HrisTimeOffTypesJobResponse) get_workforcemanagement_integrations_hris_timeofftypes_job(job_id)


Query the results of time off types job

Wraps GET /api/v2/workforcemanagement/integrations/hris/timeofftypes/jobs/{jobId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
job_id = 'job_id_example' # str | The ID of the job.

try:
    # Query the results of time off types job
    api_response = api_instance.get_workforcemanagement_integrations_hris_timeofftypes_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_integrations_hris_timeofftypes_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| The ID of the job. |  |

### Return type

[**HrisTimeOffTypesJobResponse**](HrisTimeOffTypesJobResponse)


## get_workforcemanagement_managementunit

> [**ManagementUnit**](ManagementUnit) get_workforcemanagement_managementunit(management_unit_id, expand=expand)


Get management unit

settings.shortTermForecasting is deprecated and now lives on the business unit

Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId} 

Requires ANY permissions: 

* wfm:activityCode:add
* wfm:activityCode:delete
* wfm:activityCode:edit
* wfm:activityCode:view
* wfm:agent:edit
* wfm:agentSchedule:view
* wfm:agentTimeOffRequest:submit
* wfm:agent:view
* wfm:businessUnit:add
* wfm:businessUnit:delete
* wfm:businessUnit:edit
* wfm:businessUnit:view
* wfm:historicalAdherence:view
* wfm:shrinkage:view
* wfm:intraday:view
* wfm:managementUnit:add
* wfm:managementUnit:delete
* wfm:managementUnit:edit
* wfm:managementUnit:view
* wfm:publishedSchedule:view
* wfm:realtimeAdherence:view
* wfm:schedule:add
* wfm:schedule:delete
* wfm:schedule:edit
* wfm:schedule:generate
* wfm:schedule:view
* wfm:serviceGoalTemplate:add
* wfm:serviceGoalTemplate:delete
* wfm:serviceGoalTemplate:edit
* wfm:serviceGoalTemplate:view
* wfm:planningGroup:add
* wfm:planningGroup:delete
* wfm:planningGroup:edit
* wfm:planningGroup:view
* wfm:shiftTradeRequest:edit
* wfm:shiftTradeRequest:view
* wfm:agentShiftTradeRequest:participate
* wfm:shortTermForecast:add
* wfm:shortTermForecast:delete
* wfm:shortTermForecast:edit
* wfm:shortTermForecast:view
* wfm:staffingGroup:add
* wfm:staffingGroup:delete
* wfm:staffingGroup:edit
* wfm:staffingGroup:view
* wfm:timeOffLimit:add
* wfm:timeOffLimit:delete
* wfm:timeOffLimit:edit
* wfm:timeOffLimit:view
* wfm:timeOffPlan:add
* wfm:timeOffPlan:delete
* wfm:timeOffPlan:edit
* wfm:timeOffPlan:view
* wfm:timeOffRequest:add
* wfm:timeOffRequest:edit
* wfm:timeOffRequest:view
* wfm:workPlan:add
* wfm:workPlan:delete
* wfm:workPlan:edit
* wfm:workPlan:view
* wfm:workPlanRotation:add
* wfm:workPlanRotation:delete
* wfm:workPlanRotation:edit
* wfm:workPlanRotation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
expand = ['expand_example'] # list[str] |  (optional)

try:
    # Get management unit
    api_response = api_instance.get_workforcemanagement_managementunit(management_unit_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **expand** | [**list[str]**](str)|  | [optional] <br />**Values**: settings, settings.adherence, settings.timeOff, settings.scheduling, settings.shortTermForecasting, settings.shiftTrading |

### Return type

[**ManagementUnit**](ManagementUnit)


## get_workforcemanagement_managementunit_activitycodes

> [**ActivityCodeContainer**](ActivityCodeContainer) get_workforcemanagement_managementunit_activitycodes(management_unit_id)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Deprecated: Instead use /api/v2/workforcemanagement/businessunits/{businessUnitId}/activitycodes. Get the list of activity codes

Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/activitycodes 

Requires ANY permissions: 

* wfm:activityCode:add
* wfm:activityCode:delete
* wfm:activityCode:edit
* wfm:activityCode:view
* wfm:agent:edit
* wfm:agentSchedule:view
* wfm:agentTimeOffRequest:submit
* wfm:agent:view
* wfm:businessUnit:add
* wfm:businessUnit:delete
* wfm:businessUnit:edit
* wfm:businessUnit:view
* wfm:historicalAdherence:view
* wfm:shrinkage:view
* wfm:intraday:view
* wfm:managementUnit:add
* wfm:managementUnit:delete
* wfm:managementUnit:edit
* wfm:managementUnit:view
* wfm:publishedSchedule:view
* wfm:realtimeAdherence:view
* wfm:schedule:add
* wfm:schedule:delete
* wfm:schedule:edit
* wfm:schedule:generate
* wfm:schedule:view
* wfm:shortTermForecast:add
* wfm:shortTermForecast:delete
* wfm:shortTermForecast:edit
* wfm:shortTermForecast:view
* wfm:timeOffRequest:add
* wfm:timeOffRequest:edit
* wfm:timeOffRequest:view
* wfm:workPlan:add
* wfm:workPlan:delete
* wfm:workPlan:edit
* wfm:workPlan:view
* wfm:workPlanRotation:add
* wfm:workPlanRotation:delete
* wfm:workPlanRotation:edit
* wfm:workPlanRotation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.

try:
    # Deprecated: Instead use /api/v2/workforcemanagement/businessunits/{businessUnitId}/activitycodes. Get the list of activity codes
    api_response = api_instance.get_workforcemanagement_managementunit_activitycodes(management_unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_activitycodes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |

### Return type

[**ActivityCodeContainer**](ActivityCodeContainer)


## get_workforcemanagement_managementunit_adherence

> [**UserScheduleAdherenceListing**](UserScheduleAdherenceListing) get_workforcemanagement_managementunit_adherence(management_unit_id, force_download_service=force_download_service)


Get a list of user schedule adherence records for the requested management unit

Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/adherence 

Requires ANY permissions: 

* wfm:realtimeAdherence:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit
force_download_service = True # bool | Force the result of this operation to be sent via download service.  For testing/app development purposes (optional)

try:
    # Get a list of user schedule adherence records for the requested management unit
    api_response = api_instance.get_workforcemanagement_managementunit_adherence(management_unit_id, force_download_service=force_download_service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_adherence: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit |  |
| **force_download_service** | **bool**| Force the result of this operation to be sent via download service.  For testing/app development purposes | [optional]  |

### Return type

[**UserScheduleAdherenceListing**](UserScheduleAdherenceListing)


## get_workforcemanagement_managementunit_agent

> [**WfmAgent**](WfmAgent) get_workforcemanagement_managementunit_agent(management_unit_id, agent_id, exclude_capabilities=exclude_capabilities, expand=expand)


Get data for agent in the management unit

Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/agents/{agentId} 

Requires ANY permissions: 

* wfm:agent:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
agent_id = 'agent_id_example' # str | The agent id
exclude_capabilities = True # bool | Excludes all capabilities of the agent such as queues, languages, and skills (optional)
expand = ['expand_example'] # list[str] |  (optional)

try:
    # Get data for agent in the management unit
    api_response = api_instance.get_workforcemanagement_managementunit_agent(management_unit_id, agent_id, exclude_capabilities=exclude_capabilities, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_agent: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **agent_id** | **str**| The agent id |  |
| **exclude_capabilities** | **bool**| Excludes all capabilities of the agent such as queues, languages, and skills | [optional]  |
| **expand** | [**list[str]**](str)|  | [optional] <br />**Values**: workPlanOverrides |

### Return type

[**WfmAgent**](WfmAgent)


## get_workforcemanagement_managementunit_agent_shifttrades

> [**ShiftTradeListResponse**](ShiftTradeListResponse) get_workforcemanagement_managementunit_agent_shifttrades(management_unit_id, agent_id)


Gets all the shift trades for a given agent

Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/agents/{agentId}/shifttrades 

Requires ANY permissions: 

* wfm:shiftTradeRequest:edit
* wfm:shiftTradeRequest:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
agent_id = 'agent_id_example' # str | The agent id

try:
    # Gets all the shift trades for a given agent
    api_response = api_instance.get_workforcemanagement_managementunit_agent_shifttrades(management_unit_id, agent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_agent_shifttrades: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **agent_id** | **str**| The agent id |  |

### Return type

[**ShiftTradeListResponse**](ShiftTradeListResponse)


## get_workforcemanagement_managementunit_shifttrades_matched

> [**ShiftTradeMatchesSummaryResponse**](ShiftTradeMatchesSummaryResponse) get_workforcemanagement_managementunit_shifttrades_matched(management_unit_id)


Gets a summary of all shift trades in the matched state

Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/shifttrades/matched 

Requires ANY permissions: 

* wfm:shiftTradeRequest:view
* wfm:shiftTradeRequest:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.

try:
    # Gets a summary of all shift trades in the matched state
    api_response = api_instance.get_workforcemanagement_managementunit_shifttrades_matched(management_unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_shifttrades_matched: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |

### Return type

[**ShiftTradeMatchesSummaryResponse**](ShiftTradeMatchesSummaryResponse)


## get_workforcemanagement_managementunit_shifttrades_users

> [**WfmUserEntityListing**](WfmUserEntityListing) get_workforcemanagement_managementunit_shifttrades_users(management_unit_id)


Gets list of users available for whom you can send direct shift trade requests

Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/shifttrades/users 

Requires ANY permissions: 

* wfm:agentShiftTradeRequest:participate

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.

try:
    # Gets list of users available for whom you can send direct shift trade requests
    api_response = api_instance.get_workforcemanagement_managementunit_shifttrades_users(management_unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_shifttrades_users: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |

### Return type

[**WfmUserEntityListing**](WfmUserEntityListing)


## get_workforcemanagement_managementunit_timeofflimit

> [**TimeOffLimit**](TimeOffLimit) get_workforcemanagement_managementunit_timeofflimit(management_unit_id, time_off_limit_id)


Gets a time off limit object

Returns properties of time off limit object, but not daily values.

Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/timeofflimits/{timeOffLimitId} 

Requires ANY permissions: 

* wfm:timeOffLimit:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit.
time_off_limit_id = 'time_off_limit_id_example' # str | The ID of the time off limit to fetch

try:
    # Gets a time off limit object
    api_response = api_instance.get_workforcemanagement_managementunit_timeofflimit(management_unit_id, time_off_limit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_timeofflimit: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit. |  |
| **time_off_limit_id** | **str**| The ID of the time off limit to fetch |  |

### Return type

[**TimeOffLimit**](TimeOffLimit)


## get_workforcemanagement_managementunit_timeofflimits

> [**TimeOffLimitListing**](TimeOffLimitListing) get_workforcemanagement_managementunit_timeofflimits(management_unit_id)


Gets a list of time off limit objects under management unit.

Currently only one time off limit object is allowed under management unit, so the list contains either 0 or 1 element.

Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/timeofflimits 

Requires ANY permissions: 

* wfm:timeOffLimit:view
* wfm:timeOffPlan:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit.

try:
    # Gets a list of time off limit objects under management unit.
    api_response = api_instance.get_workforcemanagement_managementunit_timeofflimits(management_unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_timeofflimits: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit. |  |

### Return type

[**TimeOffLimitListing**](TimeOffLimitListing)


## get_workforcemanagement_managementunit_timeoffplan

> [**TimeOffPlan**](TimeOffPlan) get_workforcemanagement_managementunit_timeoffplan(management_unit_id, time_off_plan_id)


Gets a time off plan

Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/timeoffplans/{timeOffPlanId} 

Requires ANY permissions: 

* wfm:timeOffPlan:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit
time_off_plan_id = 'time_off_plan_id_example' # str | The ID of the time off plan to fetch

try:
    # Gets a time off plan
    api_response = api_instance.get_workforcemanagement_managementunit_timeoffplan(management_unit_id, time_off_plan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_timeoffplan: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit |  |
| **time_off_plan_id** | **str**| The ID of the time off plan to fetch |  |

### Return type

[**TimeOffPlan**](TimeOffPlan)


## get_workforcemanagement_managementunit_timeoffplans

> [**TimeOffPlanListing**](TimeOffPlanListing) get_workforcemanagement_managementunit_timeoffplans(management_unit_id)


Gets a list of time off plans

Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/timeoffplans 

Requires ANY permissions: 

* wfm:timeOffPlan:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit

try:
    # Gets a list of time off plans
    api_response = api_instance.get_workforcemanagement_managementunit_timeoffplans(management_unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_timeoffplans: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit |  |

### Return type

[**TimeOffPlanListing**](TimeOffPlanListing)


## get_workforcemanagement_managementunit_user_timeoffrequest

> [**TimeOffRequestResponse**](TimeOffRequestResponse) get_workforcemanagement_managementunit_user_timeoffrequest(management_unit_id, user_id, time_off_request_id)


Get a time off request

Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/users/{userId}/timeoffrequests/{timeOffRequestId} 

Requires ANY permissions: 

* wfm:timeOffRequest:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
user_id = 'user_id_example' # str | The userId to whom the Time Off Request applies.
time_off_request_id = 'time_off_request_id_example' # str | Time Off Request Id

try:
    # Get a time off request
    api_response = api_instance.get_workforcemanagement_managementunit_user_timeoffrequest(management_unit_id, user_id, time_off_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_user_timeoffrequest: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **user_id** | **str**| The userId to whom the Time Off Request applies. |  |
| **time_off_request_id** | **str**| Time Off Request Id |  |

### Return type

[**TimeOffRequestResponse**](TimeOffRequestResponse)


## get_workforcemanagement_managementunit_user_timeoffrequest_timeofflimits

> [**QueryTimeOffLimitValuesResponse**](QueryTimeOffLimitValuesResponse) get_workforcemanagement_managementunit_user_timeoffrequest_timeofflimits(management_unit_id, user_id, time_off_request_id)


Retrieves time off limit, allocated and waitlisted values according to specific time off request

Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/users/{userId}/timeoffrequests/{timeOffRequestId}/timeofflimits 

Requires ALL permissions: 

* wfm:timeOffRequest:view
* wfm:timeOffLimit:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit.
user_id = 'user_id_example' # str | The userId to whom the time off request applies.
time_off_request_id = 'time_off_request_id_example' # str | The ID of the time off request, which dates and activityCodeId determine limit values to retrieve

try:
    # Retrieves time off limit, allocated and waitlisted values according to specific time off request
    api_response = api_instance.get_workforcemanagement_managementunit_user_timeoffrequest_timeofflimits(management_unit_id, user_id, time_off_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_user_timeoffrequest_timeofflimits: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit. |  |
| **user_id** | **str**| The userId to whom the time off request applies. |  |
| **time_off_request_id** | **str**| The ID of the time off request, which dates and activityCodeId determine limit values to retrieve |  |

### Return type

[**QueryTimeOffLimitValuesResponse**](QueryTimeOffLimitValuesResponse)


## get_workforcemanagement_managementunit_user_timeoffrequests

> [**TimeOffRequestList**](TimeOffRequestList) get_workforcemanagement_managementunit_user_timeoffrequests(management_unit_id, user_id)


Get a list of time off requests for a given user

Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/users/{userId}/timeoffrequests 

Requires ANY permissions: 

* wfm:timeOffRequest:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
user_id = 'user_id_example' # str | The userId to whom the Time Off Request applies.

try:
    # Get a list of time off requests for a given user
    api_response = api_instance.get_workforcemanagement_managementunit_user_timeoffrequests(management_unit_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_user_timeoffrequests: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **user_id** | **str**| The userId to whom the Time Off Request applies. |  |

### Return type

[**TimeOffRequestList**](TimeOffRequestList)


## get_workforcemanagement_managementunit_users

> [**WfmUserEntityListing**](WfmUserEntityListing) get_workforcemanagement_managementunit_users(management_unit_id)


Get users in the management unit

Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/users 

Requires ANY permissions: 

* wfm:agent:view
* wfm:historicalAdherence:view
* wfm:publishedSchedule:view
* wfm:realtimeAdherence:view
* wfm:schedule:view
* wfm:staffingGroup:view
* wfm:timeOffRequest:view
* wfm:workPlanRotation:view
* wfm:workPlan:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.

try:
    # Get users in the management unit
    api_response = api_instance.get_workforcemanagement_managementunit_users(management_unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_users: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |

### Return type

[**WfmUserEntityListing**](WfmUserEntityListing)


## get_workforcemanagement_managementunit_week_schedule

> [**WeekScheduleResponse**](WeekScheduleResponse) get_workforcemanagement_managementunit_week_schedule(management_unit_id, week_id, schedule_id, expand=expand, force_download_service=force_download_service)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Deprecated.  Use the equivalent business unit resource instead. Get a week schedule

Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekId}/schedules/{scheduleId} 

Requires ANY permissions: 

* wfm:publishedSchedule:view
* wfm:schedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
week_id = 'week_id_example' # str | First day of schedule week in yyyy-MM-dd format.
schedule_id = 'schedule_id_example' # str | The ID of the schedule to fetch
expand = 'expand_example' # str | Which fields, if any, to expand (optional)
force_download_service = True # bool | Force the result of this operation to be sent via download service.  For testing/app development purposes (optional)

try:
    # Deprecated.  Use the equivalent business unit resource instead. Get a week schedule
    api_response = api_instance.get_workforcemanagement_managementunit_week_schedule(management_unit_id, week_id, schedule_id, expand=expand, force_download_service=force_download_service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_week_schedule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **week_id** | **str**| First day of schedule week in yyyy-MM-dd format. |  |
| **schedule_id** | **str**| The ID of the schedule to fetch |  |
| **expand** | **str**| Which fields, if any, to expand | [optional] <br />**Values**: generationResults, headcountForecast |
| **force_download_service** | **bool**| Force the result of this operation to be sent via download service.  For testing/app development purposes | [optional]  |

### Return type

[**WeekScheduleResponse**](WeekScheduleResponse)


## get_workforcemanagement_managementunit_week_schedules

> [**WeekScheduleListResponse**](WeekScheduleListResponse) get_workforcemanagement_managementunit_week_schedules(management_unit_id, week_id, include_only_published=include_only_published, earliest_week_date=earliest_week_date, latest_week_date=latest_week_date)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Deprecated.  Use the equivalent business unit resource instead. Get the list of schedules in a week in management unit

Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekId}/schedules 

Requires ANY permissions: 

* wfm:publishedSchedule:view
* wfm:schedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
week_id = 'week_id_example' # str | First day of schedule week in yyyy-MM-dd format.
include_only_published = True # bool | Return only published schedules (optional)
earliest_week_date = 'earliest_week_date_example' # str | The start date of the earliest week to query in yyyy-MM-dd format (optional)
latest_week_date = 'latest_week_date_example' # str | The start date of the latest week to query in yyyy-MM-dd format (optional)

try:
    # Deprecated.  Use the equivalent business unit resource instead. Get the list of schedules in a week in management unit
    api_response = api_instance.get_workforcemanagement_managementunit_week_schedules(management_unit_id, week_id, include_only_published=include_only_published, earliest_week_date=earliest_week_date, latest_week_date=latest_week_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_week_schedules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **week_id** | **str**| First day of schedule week in yyyy-MM-dd format. |  |
| **include_only_published** | **bool**| Return only published schedules | [optional]  |
| **earliest_week_date** | **str**| The start date of the earliest week to query in yyyy-MM-dd format | [optional]  |
| **latest_week_date** | **str**| The start date of the latest week to query in yyyy-MM-dd format | [optional]  |

### Return type

[**WeekScheduleListResponse**](WeekScheduleListResponse)


## get_workforcemanagement_managementunit_week_shifttrades

> [**WeekShiftTradeListResponse**](WeekShiftTradeListResponse) get_workforcemanagement_managementunit_week_shifttrades(management_unit_id, week_date_id, evaluate_matches=evaluate_matches, force_download_service=force_download_service)


Gets all the shift trades for a given week

Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekDateId}/shifttrades 

Requires ANY permissions: 

* wfm:shiftTradeRequest:view
* wfm:shiftTradeRequest:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
week_date_id = '2013-10-20' # date | The start week date of the initiating shift in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
evaluate_matches = True # bool | Whether to evaluate the matches for violations (optional) (default to True)
force_download_service = True # bool | Force the result of this operation to be sent via download service. For testing/app development purposes (optional)

try:
    # Gets all the shift trades for a given week
    api_response = api_instance.get_workforcemanagement_managementunit_week_shifttrades(management_unit_id, week_date_id, evaluate_matches=evaluate_matches, force_download_service=force_download_service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_week_shifttrades: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **week_date_id** | **date**| The start week date of the initiating shift in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **evaluate_matches** | **bool**| Whether to evaluate the matches for violations | [optional] [default to True] |
| **force_download_service** | **bool**| Force the result of this operation to be sent via download service. For testing/app development purposes | [optional]  |

### Return type

[**WeekShiftTradeListResponse**](WeekShiftTradeListResponse)


## get_workforcemanagement_managementunit_workplan

> [**WorkPlan**](WorkPlan) get_workforcemanagement_managementunit_workplan(management_unit_id, work_plan_id, include_only=include_only)


Get a work plan

Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/workplans/{workPlanId} 

Requires ANY permissions: 

* wfm:workPlanRotation:view
* wfm:workPlan:view
* wfm:schedule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
work_plan_id = 'work_plan_id_example' # str | The ID of the work plan to fetch
include_only = ['include_only_example'] # list[str] | limit response to the specified fields (optional)

try:
    # Get a work plan
    api_response = api_instance.get_workforcemanagement_managementunit_workplan(management_unit_id, work_plan_id, include_only=include_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_workplan: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **work_plan_id** | **str**| The ID of the work plan to fetch |  |
| **include_only** | [**list[str]**](str)| limit response to the specified fields | [optional] <br />**Values**: agentCount, agents, optionalDays, shifts, shiftStartVariances |

### Return type

[**WorkPlan**](WorkPlan)


## get_workforcemanagement_managementunit_workplanrotation

> [**WorkPlanRotationResponse**](WorkPlanRotationResponse) get_workforcemanagement_managementunit_workplanrotation(management_unit_id, work_plan_rotation_id)


Get a work plan rotation

Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/workplanrotations/{workPlanRotationId} 

Requires ANY permissions: 

* wfm:workPlanRotation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
work_plan_rotation_id = 'work_plan_rotation_id_example' # str | The ID of the work plan rotation to fetch

try:
    # Get a work plan rotation
    api_response = api_instance.get_workforcemanagement_managementunit_workplanrotation(management_unit_id, work_plan_rotation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_workplanrotation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **work_plan_rotation_id** | **str**| The ID of the work plan rotation to fetch |  |

### Return type

[**WorkPlanRotationResponse**](WorkPlanRotationResponse)


## get_workforcemanagement_managementunit_workplanrotations

> [**WorkPlanRotationListResponse**](WorkPlanRotationListResponse) get_workforcemanagement_managementunit_workplanrotations(management_unit_id, expand=expand)


Get work plan rotations

Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/workplanrotations 

Requires ANY permissions: 

* wfm:agent:view
* wfm:workPlanRotation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
expand = ['expand_example'] # list[str] |  (optional)

try:
    # Get work plan rotations
    api_response = api_instance.get_workforcemanagement_managementunit_workplanrotations(management_unit_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_workplanrotations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **expand** | [**list[str]**](str)|  | [optional] <br />**Values**: agents |

### Return type

[**WorkPlanRotationListResponse**](WorkPlanRotationListResponse)


## get_workforcemanagement_managementunit_workplans

> [**WorkPlanListResponse**](WorkPlanListResponse) get_workforcemanagement_managementunit_workplans(management_unit_id, expand=expand, exclude=exclude)


Get work plans

\"expand=details\" is deprecated

Wraps GET /api/v2/workforcemanagement/managementunits/{managementUnitId}/workplans 

Requires ANY permissions: 

* wfm:agent:view
* wfm:publishedSchedule:view
* wfm:schedule:view
* wfm:workPlanRotation:view
* wfm:workPlan:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
expand = ['expand_example'] # list[str] | Include to access additional data on the work plans (optional)
exclude = ['exclude_example'] # list[str] | Exclude specific data on the work plans from the response (optional)

try:
    # Get work plans
    api_response = api_instance.get_workforcemanagement_managementunit_workplans(management_unit_id, expand=expand, exclude=exclude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunit_workplans: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **expand** | [**list[str]**](str)| Include to access additional data on the work plans | [optional] <br />**Values**: agentCount, agents, optionalDays, shifts, shiftStartVariances, details |
| **exclude** | [**list[str]**](str)| Exclude specific data on the work plans from the response | [optional] <br />**Values**: shifts.activities |

### Return type

[**WorkPlanListResponse**](WorkPlanListResponse)


## get_workforcemanagement_managementunits

> [**ManagementUnitListing**](ManagementUnitListing) get_workforcemanagement_managementunits(page_size=page_size, page_number=page_number, expand=expand, feature=feature, division_id=division_id)


Get management units

Wraps GET /api/v2/workforcemanagement/managementunits 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
page_size = 56 # int | Deprecated, paging is not supported (optional)
page_number = 56 # int | Deprecated, paging is not supported (optional)
expand = 'expand_example' # str | Deprecated, expand settings on the single MU route (optional)
feature = 'feature_example' # str | If specified, the list of management units for which the user is authorized to use the requested feature will be returned (optional)
division_id = 'division_id_example' # str | If specified, the list of management units belonging to the specified division will be returned (optional)

try:
    # Get management units
    api_response = api_instance.get_workforcemanagement_managementunits(page_size=page_size, page_number=page_number, expand=expand, feature=feature, division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunits: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **page_size** | **int**| Deprecated, paging is not supported | [optional]  |
| **page_number** | **int**| Deprecated, paging is not supported | [optional]  |
| **expand** | **str**| Deprecated, expand settings on the single MU route | [optional] <br />**Values**: details |
| **feature** | **str**| If specified, the list of management units for which the user is authorized to use the requested feature will be returned | [optional] <br />**Values**: AgentSchedule, AgentTimeOffRequest, AgentWorkPlanBid, AlternativeShift, Coaching, Learning, ActivityCodes, ActivityPlans, Agents, BuActivityCodes, BusinessUnits, CapacityPlan, ContinuousForecast, HistoricalAdherence, HistoricalShrinkage, IntradayMonitoring, BuIntradayMonitoring, ManagementUnits, RealTimeAdherence, Schedules, BuSchedules, ServiceGoalTemplates, PlanningGroups, LongTermStaffing, ShiftTrading, ShortTermForecasts, BuShortTermForecasts, StaffingGroups, TimeOffPlans, TimeOffRequests, TimeOffLimits, WorkPlanBids, WorkPlanBidGroups, WorkPlanRotations, WorkPlans |
| **division_id** | **str**| If specified, the list of management units belonging to the specified division will be returned | [optional]  |

### Return type

[**ManagementUnitListing**](ManagementUnitListing)


## get_workforcemanagement_managementunits_divisionviews

> [**ManagementUnitListing**](ManagementUnitListing) get_workforcemanagement_managementunits_divisionviews(division_id=division_id)


Get management units across divisions

Wraps GET /api/v2/workforcemanagement/managementunits/divisionviews 

Requires ANY permissions: 

* wfm:managementUnit:search

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
division_id = ['division_id_example'] # list[str] | The divisionIds to filter by. If omitted, will return all divisions (optional)

try:
    # Get management units across divisions
    api_response = api_instance.get_workforcemanagement_managementunits_divisionviews(division_id=division_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_managementunits_divisionviews: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **division_id** | [**list[str]**](str)| The divisionIds to filter by. If omitted, will return all divisions | [optional]  |

### Return type

[**ManagementUnitListing**](ManagementUnitListing)


## get_workforcemanagement_notifications

> [**NotificationsResponse**](NotificationsResponse) get_workforcemanagement_notifications()


Get a list of notifications for the current user

Notifications are only initially sent if you have the relevant Notify and Edit permissions

Wraps GET /api/v2/workforcemanagement/notifications 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()

try:
    # Get a list of notifications for the current user
    api_response = api_instance.get_workforcemanagement_notifications()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_notifications: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**NotificationsResponse**](NotificationsResponse)


## get_workforcemanagement_schedulingjob

> [**SchedulingStatusResponse**](SchedulingStatusResponse) get_workforcemanagement_schedulingjob(job_id)


Get status of the scheduling job

Wraps GET /api/v2/workforcemanagement/schedulingjobs/{jobId} 

Requires ANY permissions: 

* wfm:schedulingrequest:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
job_id = 'job_id_example' # str | The id of the scheduling job

try:
    # Get status of the scheduling job
    api_response = api_instance.get_workforcemanagement_schedulingjob(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_schedulingjob: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| The id of the scheduling job |  |

### Return type

[**SchedulingStatusResponse**](SchedulingStatusResponse)


## get_workforcemanagement_shifttrades

> [**ShiftTradeListResponse**](ShiftTradeListResponse) get_workforcemanagement_shifttrades()


Gets all of my shift trades

Wraps GET /api/v2/workforcemanagement/shifttrades 

Requires ANY permissions: 

* wfm:shiftTradeRequest:edit
* wfm:shiftTradeRequest:view
* wfm:agentShiftTradeRequest:participate

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()

try:
    # Gets all of my shift trades
    api_response = api_instance.get_workforcemanagement_shifttrades()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_shifttrades: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**ShiftTradeListResponse**](ShiftTradeListResponse)


## get_workforcemanagement_shrinkage_job

> [**WfmHistoricalShrinkageResponse**](WfmHistoricalShrinkageResponse) get_workforcemanagement_shrinkage_job(job_id)


Request to fetch the status of the historical shrinkage query

Wraps GET /api/v2/workforcemanagement/shrinkage/jobs/{jobId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
job_id = 'job_id_example' # str | jobId

try:
    # Request to fetch the status of the historical shrinkage query
    api_response = api_instance.get_workforcemanagement_shrinkage_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_shrinkage_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| jobId |  |

### Return type

[**WfmHistoricalShrinkageResponse**](WfmHistoricalShrinkageResponse)


## get_workforcemanagement_timeoffbalance_job

> [**TimeOffBalanceJobResponse**](TimeOffBalanceJobResponse) get_workforcemanagement_timeoffbalance_job(job_id)


Query the results of time off types job

Wraps GET /api/v2/workforcemanagement/timeoffbalance/jobs/{jobId} 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
job_id = 'job_id_example' # str | The ID of the job.

try:
    # Query the results of time off types job
    api_response = api_instance.get_workforcemanagement_timeoffbalance_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_timeoffbalance_job: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **job_id** | **str**| The ID of the job. |  |

### Return type

[**TimeOffBalanceJobResponse**](TimeOffBalanceJobResponse)


## get_workforcemanagement_timeoffrequest

> [**TimeOffRequestResponse**](TimeOffRequestResponse) get_workforcemanagement_timeoffrequest(time_off_request_id)


Get a time off request for the current user

Wraps GET /api/v2/workforcemanagement/timeoffrequests/{timeOffRequestId} 

Requires ANY permissions: 

* wfm:agentSchedule:view
* wfm:agentTimeOffRequest:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
time_off_request_id = 'time_off_request_id_example' # str | The ID of the time off request

try:
    # Get a time off request for the current user
    api_response = api_instance.get_workforcemanagement_timeoffrequest(time_off_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_timeoffrequest: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **time_off_request_id** | **str**| The ID of the time off request |  |

### Return type

[**TimeOffRequestResponse**](TimeOffRequestResponse)


## get_workforcemanagement_timeoffrequest_waitlistpositions

> [**WaitlistPositionListing**](WaitlistPositionListing) get_workforcemanagement_timeoffrequest_waitlistpositions(time_off_request_id)


Get the daily waitlist positions of a time off request for the current user

Wraps GET /api/v2/workforcemanagement/timeoffrequests/{timeOffRequestId}/waitlistpositions 

Requires ANY permissions: 

* wfm:agentTimeOffRequest:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
time_off_request_id = 'time_off_request_id_example' # str | The ID of the time off request

try:
    # Get the daily waitlist positions of a time off request for the current user
    api_response = api_instance.get_workforcemanagement_timeoffrequest_waitlistpositions(time_off_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_timeoffrequest_waitlistpositions: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **time_off_request_id** | **str**| The ID of the time off request |  |

### Return type

[**WaitlistPositionListing**](WaitlistPositionListing)


## get_workforcemanagement_timeoffrequests

> [**TimeOffRequestList**](TimeOffRequestList) get_workforcemanagement_timeoffrequests()


Get a list of time off requests for the current user

Wraps GET /api/v2/workforcemanagement/timeoffrequests 

Requires ANY permissions: 

* wfm:agentSchedule:view
* wfm:agentTimeOffRequest:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()

try:
    # Get a list of time off requests for the current user
    api_response = api_instance.get_workforcemanagement_timeoffrequests()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_timeoffrequests: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**TimeOffRequestList**](TimeOffRequestList)


## get_workforcemanagement_user_workplanbidranks

> [**WorkPlanBidRanks**](WorkPlanBidRanks) get_workforcemanagement_user_workplanbidranks(user_id)


Get work plan bid ranks for a user

Wraps GET /api/v2/workforcemanagement/users/{userId}/workplanbidranks 

Requires ANY permissions: 

* wfm:workPlanBid:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
user_id = 'user_id_example' # str | The userId to whom the work plan bid ranks apply.

try:
    # Get work plan bid ranks for a user
    api_response = api_instance.get_workforcemanagement_user_workplanbidranks(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_user_workplanbidranks: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| The userId to whom the work plan bid ranks apply. |  |

### Return type

[**WorkPlanBidRanks**](WorkPlanBidRanks)


## get_workforcemanagement_workplanbid_preferences

> [**AgentWorkPlanBiddingPreferenceResponse**](AgentWorkPlanBiddingPreferenceResponse) get_workforcemanagement_workplanbid_preferences(bid_id)


Gets an agent's work plan bidding preference

Wraps GET /api/v2/workforcemanagement/workplanbids/{bidId}/preferences 

Requires ANY permissions: 

* wfm:agentWorkPlanBid:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
bid_id = 'bid_id_example' # str | The ID of the work plan bid

try:
    # Gets an agent's work plan bidding preference
    api_response = api_instance.get_workforcemanagement_workplanbid_preferences(bid_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_workplanbid_preferences: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bid_id** | **str**| The ID of the work plan bid |  |

### Return type

[**AgentWorkPlanBiddingPreferenceResponse**](AgentWorkPlanBiddingPreferenceResponse)


## get_workforcemanagement_workplanbid_workplans

> [**AgentWorkPlanListResponse**](AgentWorkPlanListResponse) get_workforcemanagement_workplanbid_workplans(bid_id)


Gets an agent's work plans for a bid

Wraps GET /api/v2/workforcemanagement/workplanbids/{bidId}/workplans 

Requires ANY permissions: 

* wfm:agentWorkPlanBid:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
bid_id = 'bid_id_example' # str | The ID of the work plan bid

try:
    # Gets an agent's work plans for a bid
    api_response = api_instance.get_workforcemanagement_workplanbid_workplans(bid_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_workplanbid_workplans: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bid_id** | **str**| The ID of the work plan bid |  |

### Return type

[**AgentWorkPlanListResponse**](AgentWorkPlanListResponse)


## get_workforcemanagement_workplanbids

> [**AgentWorkPlanBids**](AgentWorkPlanBids) get_workforcemanagement_workplanbids()


Gets the list of work plan bids that belong to an agent

Wraps GET /api/v2/workforcemanagement/workplanbids 

Requires ANY permissions: 

* wfm:agentWorkPlanBid:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()

try:
    # Gets the list of work plan bids that belong to an agent
    api_response = api_instance.get_workforcemanagement_workplanbids()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->get_workforcemanagement_workplanbids: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**AgentWorkPlanBids**](AgentWorkPlanBids)


## patch_workforcemanagement_agent_adherence_explanation

> [**AdherenceExplanationAsyncResponse**](AdherenceExplanationAsyncResponse) patch_workforcemanagement_agent_adherence_explanation(agent_id, explanation_id, body)


Update an adherence explanation

Wraps PATCH /api/v2/workforcemanagement/agents/{agentId}/adherence/explanations/{explanationId} 

Requires ANY permissions: 

* wfm:adherenceExplanation:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
agent_id = 'agent_id_example' # str | The ID of the agent to query
explanation_id = 'explanation_id_example' # str | The ID of the explanation to update
body = PureCloudPlatformClientV2.UpdateAdherenceExplanationStatusRequest() # UpdateAdherenceExplanationStatusRequest | The request body

try:
    # Update an adherence explanation
    api_response = api_instance.patch_workforcemanagement_agent_adherence_explanation(agent_id, explanation_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_agent_adherence_explanation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str**| The ID of the agent to query |  |
| **explanation_id** | **str**| The ID of the explanation to update |  |
| **body** | [**UpdateAdherenceExplanationStatusRequest**](UpdateAdherenceExplanationStatusRequest)| The request body |  |

### Return type

[**AdherenceExplanationAsyncResponse**](AdherenceExplanationAsyncResponse)


## patch_workforcemanagement_alternativeshifts_trade

> [**AlternativeShiftTradeResponse**](AlternativeShiftTradeResponse) patch_workforcemanagement_alternativeshifts_trade(trade_id, body=body)


Update my alternative shifts trade by trade ID

Wraps PATCH /api/v2/workforcemanagement/alternativeshifts/trades/{tradeId} 

Requires ANY permissions: 

* wfm:agentAlternativeShift:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
trade_id = 'trade_id_example' # str | The ID of the alternative shift trade
body = PureCloudPlatformClientV2.AgentUpdateAlternativeShiftTradeRequest() # AgentUpdateAlternativeShiftTradeRequest | body (optional)

try:
    # Update my alternative shifts trade by trade ID
    api_response = api_instance.patch_workforcemanagement_alternativeshifts_trade(trade_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_alternativeshifts_trade: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **trade_id** | **str**| The ID of the alternative shift trade |  |
| **body** | [**AgentUpdateAlternativeShiftTradeRequest**](AgentUpdateAlternativeShiftTradeRequest)| body | [optional]  |

### Return type

[**AlternativeShiftTradeResponse**](AlternativeShiftTradeResponse)


## patch_workforcemanagement_alternativeshifts_trades_state_jobs

> [**AlternativeShiftAsyncResponse**](AlternativeShiftAsyncResponse) patch_workforcemanagement_alternativeshifts_trades_state_jobs(body)


Bulk update alternative shift trade states

Wraps PATCH /api/v2/workforcemanagement/alternativeshifts/trades/state/jobs 

Requires ANY permissions: 

* wfm:alternativeShift:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.AdminBulkUpdateAlternativeShiftTradeStateRequest() # AdminBulkUpdateAlternativeShiftTradeStateRequest | The request body

try:
    # Bulk update alternative shift trade states
    api_response = api_instance.patch_workforcemanagement_alternativeshifts_trades_state_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_alternativeshifts_trades_state_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AdminBulkUpdateAlternativeShiftTradeStateRequest**](AdminBulkUpdateAlternativeShiftTradeStateRequest)| The request body |  |

### Return type

[**AlternativeShiftAsyncResponse**](AlternativeShiftAsyncResponse)


## patch_workforcemanagement_businessunit

> [**BusinessUnitResponse**](BusinessUnitResponse) patch_workforcemanagement_businessunit(business_unit_id, body=body)


Update business unit

Wraps PATCH /api/v2/workforcemanagement/businessunits/{businessUnitId} 

Requires ALL permissions: 

* wfm:businessUnit:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit, or 'mine' for the business unit of the logged-in user.
body = PureCloudPlatformClientV2.UpdateBusinessUnitRequest() # UpdateBusinessUnitRequest | body (optional)

try:
    # Update business unit
    api_response = api_instance.patch_workforcemanagement_businessunit(business_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_businessunit: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit, or &#39;mine&#39; for the business unit of the logged-in user. |  |
| **body** | [**UpdateBusinessUnitRequest**](UpdateBusinessUnitRequest)| body | [optional]  |

### Return type

[**BusinessUnitResponse**](BusinessUnitResponse)


## patch_workforcemanagement_businessunit_activitycode

> [**BusinessUnitActivityCode**](BusinessUnitActivityCode) patch_workforcemanagement_businessunit_activitycode(business_unit_id, activity_code_id, body=body)


Update an activity code

Wraps PATCH /api/v2/workforcemanagement/businessunits/{businessUnitId}/activitycodes/{activityCodeId} 

Requires ANY permissions: 

* wfm:activityCode:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit, or 'mine' for the business unit of the logged-in user.
activity_code_id = 'activity_code_id_example' # str | The ID of the activity code to update
body = PureCloudPlatformClientV2.UpdateActivityCodeRequest() # UpdateActivityCodeRequest | body (optional)

try:
    # Update an activity code
    api_response = api_instance.patch_workforcemanagement_businessunit_activitycode(business_unit_id, activity_code_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_businessunit_activitycode: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit, or &#39;mine&#39; for the business unit of the logged-in user. |  |
| **activity_code_id** | **str**| The ID of the activity code to update |  |
| **body** | [**UpdateActivityCodeRequest**](UpdateActivityCodeRequest)| body | [optional]  |

### Return type

[**BusinessUnitActivityCode**](BusinessUnitActivityCode)


## patch_workforcemanagement_businessunit_activityplan

> [**ActivityPlanResponse**](ActivityPlanResponse) patch_workforcemanagement_businessunit_activityplan(business_unit_id, activity_plan_id, body)


Update an activity plan

If a job associated with the activity plan is in 'Processing' state the activity plan cannot be updated

Wraps PATCH /api/v2/workforcemanagement/businessunits/{businessUnitId}/activityplans/{activityPlanId} 

Requires ANY permissions: 

* wfm:activityPlan:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
activity_plan_id = 'activity_plan_id_example' # str | The ID of the activity plan to update
body = PureCloudPlatformClientV2.UpdateActivityPlanRequest() # UpdateActivityPlanRequest | body

try:
    # Update an activity plan
    api_response = api_instance.patch_workforcemanagement_businessunit_activityplan(business_unit_id, activity_plan_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_businessunit_activityplan: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **activity_plan_id** | **str**| The ID of the activity plan to update |  |
| **body** | [**UpdateActivityPlanRequest**](UpdateActivityPlanRequest)| body |  |

### Return type

[**ActivityPlanResponse**](ActivityPlanResponse)


## patch_workforcemanagement_businessunit_alternativeshifts_settings

> [**AlternativeShiftBuSettingsResponse**](AlternativeShiftBuSettingsResponse) patch_workforcemanagement_businessunit_alternativeshifts_settings(business_unit_id, body=body)


Update alternative shifts settings for a business unit

Wraps PATCH /api/v2/workforcemanagement/businessunits/{businessUnitId}/alternativeshifts/settings 

Requires ANY permissions: 

* wfm:businessUnit:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
body = PureCloudPlatformClientV2.UpdateAlternativeShiftBuSettingsRequest() # UpdateAlternativeShiftBuSettingsRequest | body (optional)

try:
    # Update alternative shifts settings for a business unit
    api_response = api_instance.patch_workforcemanagement_businessunit_alternativeshifts_settings(business_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_businessunit_alternativeshifts_settings: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **body** | [**UpdateAlternativeShiftBuSettingsRequest**](UpdateAlternativeShiftBuSettingsRequest)| body | [optional]  |

### Return type

[**AlternativeShiftBuSettingsResponse**](AlternativeShiftBuSettingsResponse)


## patch_workforcemanagement_businessunit_planninggroup

> [**PlanningGroup**](PlanningGroup) patch_workforcemanagement_businessunit_planninggroup(business_unit_id, planning_group_id, body=body)


Updates the planning group

Wraps PATCH /api/v2/workforcemanagement/businessunits/{businessUnitId}/planninggroups/{planningGroupId} 

Requires ANY permissions: 

* wfm:planningGroup:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit.
planning_group_id = 'planning_group_id_example' # str | The ID of a planning group to update
body = PureCloudPlatformClientV2.UpdatePlanningGroupRequest() # UpdatePlanningGroupRequest | body (optional)

try:
    # Updates the planning group
    api_response = api_instance.patch_workforcemanagement_businessunit_planninggroup(business_unit_id, planning_group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_businessunit_planninggroup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit. |  |
| **planning_group_id** | **str**| The ID of a planning group to update |  |
| **body** | [**UpdatePlanningGroupRequest**](UpdatePlanningGroupRequest)| body | [optional]  |

### Return type

[**PlanningGroup**](PlanningGroup)


## patch_workforcemanagement_businessunit_scheduling_run

>  patch_workforcemanagement_businessunit_scheduling_run(business_unit_id, run_id, body=body)


Mark a schedule run as applied

Wraps PATCH /api/v2/workforcemanagement/businessunits/{businessUnitId}/scheduling/runs/{runId} 

Requires ANY permissions: 

* wfm:schedule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
run_id = 'run_id_example' # str | The ID of the schedule run
body = PureCloudPlatformClientV2.PatchBuScheduleRunRequest() # PatchBuScheduleRunRequest | body (optional)

try:
    # Mark a schedule run as applied
    api_instance.patch_workforcemanagement_businessunit_scheduling_run(business_unit_id, run_id, body=body)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_businessunit_scheduling_run: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **run_id** | **str**| The ID of the schedule run |  |
| **body** | [**PatchBuScheduleRunRequest**](PatchBuScheduleRunRequest)| body | [optional]  |

### Return type

void (empty response body)


## patch_workforcemanagement_businessunit_servicegoaltemplate

> [**ServiceGoalTemplate**](ServiceGoalTemplate) patch_workforcemanagement_businessunit_servicegoaltemplate(business_unit_id, service_goal_template_id, body=body)


Updates a service goal template

Wraps PATCH /api/v2/workforcemanagement/businessunits/{businessUnitId}/servicegoaltemplates/{serviceGoalTemplateId} 

Requires ANY permissions: 

* wfm:serviceGoalTemplate:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit.
service_goal_template_id = 'service_goal_template_id_example' # str | The ID of a service goal template to update
body = PureCloudPlatformClientV2.UpdateServiceGoalTemplate() # UpdateServiceGoalTemplate | body (optional)

try:
    # Updates a service goal template
    api_response = api_instance.patch_workforcemanagement_businessunit_servicegoaltemplate(business_unit_id, service_goal_template_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_businessunit_servicegoaltemplate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit. |  |
| **service_goal_template_id** | **str**| The ID of a service goal template to update |  |
| **body** | [**UpdateServiceGoalTemplate**](UpdateServiceGoalTemplate)| body | [optional]  |

### Return type

[**ServiceGoalTemplate**](ServiceGoalTemplate)


## patch_workforcemanagement_businessunit_staffinggroup

> [**StaffingGroupResponse**](StaffingGroupResponse) patch_workforcemanagement_businessunit_staffinggroup(business_unit_id, staffing_group_id, body=body)


Updates a staffing group

Wraps PATCH /api/v2/workforcemanagement/businessunits/{businessUnitId}/staffinggroups/{staffingGroupId} 

Requires ANY permissions: 

* wfm:staffingGroup:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
staffing_group_id = 'staffing_group_id_example' # str | The ID of the staffing group to update
body = PureCloudPlatformClientV2.UpdateStaffingGroupRequest() # UpdateStaffingGroupRequest | body (optional)

try:
    # Updates a staffing group
    api_response = api_instance.patch_workforcemanagement_businessunit_staffinggroup(business_unit_id, staffing_group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_businessunit_staffinggroup: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **staffing_group_id** | **str**| The ID of the staffing group to update |  |
| **body** | [**UpdateStaffingGroupRequest**](UpdateStaffingGroupRequest)| body | [optional]  |

### Return type

[**StaffingGroupResponse**](StaffingGroupResponse)


## patch_workforcemanagement_businessunit_timeoffplan

> [**BuTimeOffPlanResponse**](BuTimeOffPlanResponse) patch_workforcemanagement_businessunit_timeoffplan(business_unit_id, time_off_plan_id, body=body)


Updates a time-off plan

Wraps PATCH /api/v2/workforcemanagement/businessunits/{businessUnitId}/timeoffplans/{timeOffPlanId} 

Requires ANY permissions: 

* wfm:timeOffPlan:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
time_off_plan_id = 'time_off_plan_id_example' # str | The ID of the time-off plan to update
body = PureCloudPlatformClientV2.BuUpdateTimeOffPlanRequest() # BuUpdateTimeOffPlanRequest | body (optional)

try:
    # Updates a time-off plan
    api_response = api_instance.patch_workforcemanagement_businessunit_timeoffplan(business_unit_id, time_off_plan_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_businessunit_timeoffplan: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **time_off_plan_id** | **str**| The ID of the time-off plan to update |  |
| **body** | [**BuUpdateTimeOffPlanRequest**](BuUpdateTimeOffPlanRequest)| body | [optional]  |

### Return type

[**BuTimeOffPlanResponse**](BuTimeOffPlanResponse)


## patch_workforcemanagement_businessunit_workplanbid

> [**WorkPlanBid**](WorkPlanBid) patch_workforcemanagement_businessunit_workplanbid(business_unit_id, bid_id, body)


Update work plan bid

Wraps PATCH /api/v2/workforcemanagement/businessunits/{businessUnitId}/workplanbids/{bidId} 

Requires ANY permissions: 

* wfm:workPlanBid:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
bid_id = 'bid_id_example' # str | The id of the workplanbid
body = PureCloudPlatformClientV2.UpdateWorkPlanBid() # UpdateWorkPlanBid | The work plan bid to be updated

try:
    # Update work plan bid
    api_response = api_instance.patch_workforcemanagement_businessunit_workplanbid(business_unit_id, bid_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_businessunit_workplanbid: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **bid_id** | **str**| The id of the workplanbid |  |
| **body** | [**UpdateWorkPlanBid**](UpdateWorkPlanBid)| The work plan bid to be updated |  |

### Return type

[**WorkPlanBid**](WorkPlanBid)


## patch_workforcemanagement_businessunit_workplanbid_group

> [**WorkPlanBidGroupResponse**](WorkPlanBidGroupResponse) patch_workforcemanagement_businessunit_workplanbid_group(business_unit_id, bid_id, bid_group_id, body=body)


Update a bid group by bid group Id

Wraps PATCH /api/v2/workforcemanagement/businessunits/{businessUnitId}/workplanbids/{bidId}/groups/{bidGroupId} 

Requires ANY permissions: 

* wfm:workPlanBidGroup:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
bid_id = 'bid_id_example' # str | The work plan bid id of the bid groups
bid_group_id = 'bid_group_id_example' # str | Work Plan Bid Group id
body = PureCloudPlatformClientV2.WorkPlanBidGroupUpdate() # WorkPlanBidGroupUpdate | body (optional)

try:
    # Update a bid group by bid group Id
    api_response = api_instance.patch_workforcemanagement_businessunit_workplanbid_group(business_unit_id, bid_id, bid_group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_businessunit_workplanbid_group: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **bid_id** | **str**| The work plan bid id of the bid groups |  |
| **bid_group_id** | **str**| Work Plan Bid Group id |  |
| **body** | [**WorkPlanBidGroupUpdate**](WorkPlanBidGroupUpdate)| body | [optional]  |

### Return type

[**WorkPlanBidGroupResponse**](WorkPlanBidGroupResponse)


## patch_workforcemanagement_businessunit_workplanbid_group_preferences

> [**AdminAgentWorkPlanPreferenceResponse**](AdminAgentWorkPlanPreferenceResponse) patch_workforcemanagement_businessunit_workplanbid_group_preferences(business_unit_id, bid_id, bid_group_id, body=body)


Overrides the assigned work plan for the specified agents

Wraps PATCH /api/v2/workforcemanagement/businessunits/{businessUnitId}/workplanbids/{bidId}/groups/{bidGroupId}/preferences 

Requires ANY permissions: 

* wfm:workPlanBidGroup:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
bid_id = 'bid_id_example' # str | The work plan bid id of the bid groups
bid_group_id = 'bid_group_id_example' # str | The ID of the work plan bid group
body = PureCloudPlatformClientV2.AgentsBidAssignedWorkPlanOverrideRequest() # AgentsBidAssignedWorkPlanOverrideRequest | body (optional)

try:
    # Overrides the assigned work plan for the specified agents
    api_response = api_instance.patch_workforcemanagement_businessunit_workplanbid_group_preferences(business_unit_id, bid_id, bid_group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_businessunit_workplanbid_group_preferences: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **bid_id** | **str**| The work plan bid id of the bid groups |  |
| **bid_group_id** | **str**| The ID of the work plan bid group |  |
| **body** | [**AgentsBidAssignedWorkPlanOverrideRequest**](AgentsBidAssignedWorkPlanOverrideRequest)| body | [optional]  |

### Return type

[**AdminAgentWorkPlanPreferenceResponse**](AdminAgentWorkPlanPreferenceResponse)


## patch_workforcemanagement_managementunit

> [**ManagementUnit**](ManagementUnit) patch_workforcemanagement_managementunit(management_unit_id, body=body)


Update the requested management unit

Wraps PATCH /api/v2/workforcemanagement/managementunits/{managementUnitId} 

Requires ANY permissions: 

* wfm:managementUnit:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
body = PureCloudPlatformClientV2.UpdateManagementUnitRequest() # UpdateManagementUnitRequest | body (optional)

try:
    # Update the requested management unit
    api_response = api_instance.patch_workforcemanagement_managementunit(management_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_managementunit: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **body** | [**UpdateManagementUnitRequest**](UpdateManagementUnitRequest)| body | [optional]  |

### Return type

[**ManagementUnit**](ManagementUnit)


## patch_workforcemanagement_managementunit_agents

>  patch_workforcemanagement_managementunit_agents(management_unit_id, body=body)


Update agent configurations

Wraps PATCH /api/v2/workforcemanagement/managementunits/{managementUnitId}/agents 

Requires ANY permissions: 

* wfm:agent:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
body = PureCloudPlatformClientV2.UpdateMuAgentsRequest() # UpdateMuAgentsRequest | body (optional)

try:
    # Update agent configurations
    api_instance.patch_workforcemanagement_managementunit_agents(management_unit_id, body=body)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_managementunit_agents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **body** | [**UpdateMuAgentsRequest**](UpdateMuAgentsRequest)| body | [optional]  |

### Return type

void (empty response body)


## patch_workforcemanagement_managementunit_agents_workplans_bulk

> [**UpdateMuAgentWorkPlansBatchResponse**](UpdateMuAgentWorkPlansBatchResponse) patch_workforcemanagement_managementunit_agents_workplans_bulk(management_unit_id, body=body)


Updates agent work plan configuration

Wraps PATCH /api/v2/workforcemanagement/managementunits/{managementUnitId}/agents/workplans/bulk 

Requires ANY permissions: 

* wfm:workPlan:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
body = PureCloudPlatformClientV2.UpdateMuAgentWorkPlansBatchRequest() # UpdateMuAgentWorkPlansBatchRequest | body (optional)

try:
    # Updates agent work plan configuration
    api_response = api_instance.patch_workforcemanagement_managementunit_agents_workplans_bulk(management_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_managementunit_agents_workplans_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **body** | [**UpdateMuAgentWorkPlansBatchRequest**](UpdateMuAgentWorkPlansBatchRequest)| body | [optional]  |

### Return type

[**UpdateMuAgentWorkPlansBatchResponse**](UpdateMuAgentWorkPlansBatchResponse)


## patch_workforcemanagement_managementunit_timeofflimit

> [**TimeOffLimit**](TimeOffLimit) patch_workforcemanagement_managementunit_timeofflimit(management_unit_id, time_off_limit_id, body=body)


Updates a time off limit object.

Updates time off limit object properties, but not daily values.

Wraps PATCH /api/v2/workforcemanagement/managementunits/{managementUnitId}/timeofflimits/{timeOffLimitId} 

Requires ANY permissions: 

* wfm:timeOffLimit:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit.
time_off_limit_id = 'time_off_limit_id_example' # str | The id of time off limit object to update
body = PureCloudPlatformClientV2.UpdateTimeOffLimitRequest() # UpdateTimeOffLimitRequest | body (optional)

try:
    # Updates a time off limit object.
    api_response = api_instance.patch_workforcemanagement_managementunit_timeofflimit(management_unit_id, time_off_limit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_managementunit_timeofflimit: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit. |  |
| **time_off_limit_id** | **str**| The id of time off limit object to update |  |
| **body** | [**UpdateTimeOffLimitRequest**](UpdateTimeOffLimitRequest)| body | [optional]  |

### Return type

[**TimeOffLimit**](TimeOffLimit)


## patch_workforcemanagement_managementunit_timeoffplan

> [**TimeOffPlan**](TimeOffPlan) patch_workforcemanagement_managementunit_timeoffplan(management_unit_id, time_off_plan_id, body=body)


Updates a time off plan

Wraps PATCH /api/v2/workforcemanagement/managementunits/{managementUnitId}/timeoffplans/{timeOffPlanId} 

Requires ANY permissions: 

* wfm:timeOffPlan:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit
time_off_plan_id = 'time_off_plan_id_example' # str | The ID of the time off plan to update
body = PureCloudPlatformClientV2.UpdateTimeOffPlanRequest() # UpdateTimeOffPlanRequest | body (optional)

try:
    # Updates a time off plan
    api_response = api_instance.patch_workforcemanagement_managementunit_timeoffplan(management_unit_id, time_off_plan_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_managementunit_timeoffplan: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit |  |
| **time_off_plan_id** | **str**| The ID of the time off plan to update |  |
| **body** | [**UpdateTimeOffPlanRequest**](UpdateTimeOffPlanRequest)| body | [optional]  |

### Return type

[**TimeOffPlan**](TimeOffPlan)


## patch_workforcemanagement_managementunit_timeoffrequest_user_integrationstatus

> [**UserTimeOffIntegrationStatusResponse**](UserTimeOffIntegrationStatusResponse) patch_workforcemanagement_managementunit_timeoffrequest_user_integrationstatus(management_unit_id, time_off_request_id, user_id, body=body)


Set integration status for a time off request.

Wraps PATCH /api/v2/workforcemanagement/managementunits/{managementUnitId}/timeoffrequests/{timeOffRequestId}/users/{userId}/integrationstatus 

Requires ANY permissions: 

* wfm:timeOffRequest:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit.
time_off_request_id = 'time_off_request_id_example' # str | The ID of the time off request.
user_id = 'user_id_example' # str | The ID of user to whom the time off request belongs.
body = PureCloudPlatformClientV2.SetTimeOffIntegrationStatusRequest() # SetTimeOffIntegrationStatusRequest | body (optional)

try:
    # Set integration status for a time off request.
    api_response = api_instance.patch_workforcemanagement_managementunit_timeoffrequest_user_integrationstatus(management_unit_id, time_off_request_id, user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_managementunit_timeoffrequest_user_integrationstatus: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit. |  |
| **time_off_request_id** | **str**| The ID of the time off request. |  |
| **user_id** | **str**| The ID of user to whom the time off request belongs. |  |
| **body** | [**SetTimeOffIntegrationStatusRequest**](SetTimeOffIntegrationStatusRequest)| body | [optional]  |

### Return type

[**UserTimeOffIntegrationStatusResponse**](UserTimeOffIntegrationStatusResponse)


## patch_workforcemanagement_managementunit_user_timeoffrequest

> [**TimeOffRequestResponse**](TimeOffRequestResponse) patch_workforcemanagement_managementunit_user_timeoffrequest(management_unit_id, user_id, time_off_request_id, body=body)


Update a time off request

Wraps PATCH /api/v2/workforcemanagement/managementunits/{managementUnitId}/users/{userId}/timeoffrequests/{timeOffRequestId} 

Requires ANY permissions: 

* wfm:timeOffRequest:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
user_id = 'user_id_example' # str | The id of the user the requested time off request belongs to
time_off_request_id = 'time_off_request_id_example' # str | The id of the time off request to update
body = PureCloudPlatformClientV2.AdminTimeOffRequestPatch() # AdminTimeOffRequestPatch | body (optional)

try:
    # Update a time off request
    api_response = api_instance.patch_workforcemanagement_managementunit_user_timeoffrequest(management_unit_id, user_id, time_off_request_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_managementunit_user_timeoffrequest: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **user_id** | **str**| The id of the user the requested time off request belongs to |  |
| **time_off_request_id** | **str**| The id of the time off request to update |  |
| **body** | [**AdminTimeOffRequestPatch**](AdminTimeOffRequestPatch)| body | [optional]  |

### Return type

[**TimeOffRequestResponse**](TimeOffRequestResponse)


## patch_workforcemanagement_managementunit_week_shifttrade

> [**ShiftTradeResponse**](ShiftTradeResponse) patch_workforcemanagement_managementunit_week_shifttrade(management_unit_id, week_date_id, trade_id, body)


Updates a shift trade. This route can only be called by the initiating agent

Wraps PATCH /api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekDateId}/shifttrades/{tradeId} 

Requires ANY permissions: 

* wfm:agentShiftTradeRequest:participate

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
week_date_id = '2013-10-20' # date | The start week date of the initiating shift in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
trade_id = 'trade_id_example' # str | The ID of the shift trade to update
body = PureCloudPlatformClientV2.PatchShiftTradeRequest() # PatchShiftTradeRequest | body

try:
    # Updates a shift trade. This route can only be called by the initiating agent
    api_response = api_instance.patch_workforcemanagement_managementunit_week_shifttrade(management_unit_id, week_date_id, trade_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_managementunit_week_shifttrade: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **week_date_id** | **date**| The start week date of the initiating shift in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **trade_id** | **str**| The ID of the shift trade to update |  |
| **body** | [**PatchShiftTradeRequest**](PatchShiftTradeRequest)| body |  |

### Return type

[**ShiftTradeResponse**](ShiftTradeResponse)


## patch_workforcemanagement_managementunit_workplan

> [**WorkPlan**](WorkPlan) patch_workforcemanagement_managementunit_workplan(management_unit_id, work_plan_id, validation_mode=validation_mode, body=body)


Update a work plan

Wraps PATCH /api/v2/workforcemanagement/managementunits/{managementUnitId}/workplans/{workPlanId} 

Requires ANY permissions: 

* wfm:workPlan:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
work_plan_id = 'work_plan_id_example' # str | The ID of the work plan to update
validation_mode = 'validation_mode_example' # str | Allows to update work plan even if validation result is invalid (optional)
body = PureCloudPlatformClientV2.WorkPlan() # WorkPlan | body (optional)

try:
    # Update a work plan
    api_response = api_instance.patch_workforcemanagement_managementunit_workplan(management_unit_id, work_plan_id, validation_mode=validation_mode, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_managementunit_workplan: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **work_plan_id** | **str**| The ID of the work plan to update |  |
| **validation_mode** | **str**| Allows to update work plan even if validation result is invalid | [optional] <br />**Values**: Ignore |
| **body** | [**WorkPlan**](WorkPlan)| body | [optional]  |

### Return type

[**WorkPlan**](WorkPlan)


## patch_workforcemanagement_managementunit_workplanrotation

> [**WorkPlanRotationResponse**](WorkPlanRotationResponse) patch_workforcemanagement_managementunit_workplanrotation(management_unit_id, work_plan_rotation_id, body=body)


Update a work plan rotation

Wraps PATCH /api/v2/workforcemanagement/managementunits/{managementUnitId}/workplanrotations/{workPlanRotationId} 

Requires ANY permissions: 

* wfm:workPlanRotation:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
work_plan_rotation_id = 'work_plan_rotation_id_example' # str | The ID of the work plan rotation to update
body = PureCloudPlatformClientV2.UpdateWorkPlanRotationRequest() # UpdateWorkPlanRotationRequest | body (optional)

try:
    # Update a work plan rotation
    api_response = api_instance.patch_workforcemanagement_managementunit_workplanrotation(management_unit_id, work_plan_rotation_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_managementunit_workplanrotation: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **work_plan_rotation_id** | **str**| The ID of the work plan rotation to update |  |
| **body** | [**UpdateWorkPlanRotationRequest**](UpdateWorkPlanRotationRequest)| body | [optional]  |

### Return type

[**WorkPlanRotationResponse**](WorkPlanRotationResponse)


## patch_workforcemanagement_timeoffrequest

> [**TimeOffRequestResponse**](TimeOffRequestResponse) patch_workforcemanagement_timeoffrequest(time_off_request_id, body=body)


Update a time off request for the current user

Wraps PATCH /api/v2/workforcemanagement/timeoffrequests/{timeOffRequestId} 

Requires ANY permissions: 

* wfm:agentTimeOffRequest:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
time_off_request_id = 'time_off_request_id_example' # str | The ID of the time off request
body = PureCloudPlatformClientV2.AgentTimeOffRequestPatch() # AgentTimeOffRequestPatch | body (optional)

try:
    # Update a time off request for the current user
    api_response = api_instance.patch_workforcemanagement_timeoffrequest(time_off_request_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_timeoffrequest: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **time_off_request_id** | **str**| The ID of the time off request |  |
| **body** | [**AgentTimeOffRequestPatch**](AgentTimeOffRequestPatch)| body | [optional]  |

### Return type

[**TimeOffRequestResponse**](TimeOffRequestResponse)


## patch_workforcemanagement_user_workplanbidranks

> [**WorkPlanBidRanks**](WorkPlanBidRanks) patch_workforcemanagement_user_workplanbidranks(user_id, body=body)


Update work plan bid ranks for a user

Wraps PATCH /api/v2/workforcemanagement/users/{userId}/workplanbidranks 

Requires ANY permissions: 

* wfm:workPlanBid:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
user_id = 'user_id_example' # str | The userId to whom the work plan bid ranks apply.
body = PureCloudPlatformClientV2.WorkPlanBidRanks() # WorkPlanBidRanks | body (optional)

try:
    # Update work plan bid ranks for a user
    api_response = api_instance.patch_workforcemanagement_user_workplanbidranks(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_user_workplanbidranks: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user_id** | **str**| The userId to whom the work plan bid ranks apply. |  |
| **body** | [**WorkPlanBidRanks**](WorkPlanBidRanks)| body | [optional]  |

### Return type

[**WorkPlanBidRanks**](WorkPlanBidRanks)


## patch_workforcemanagement_users_workplanbidranks_bulk

> [**EntityListing**](EntityListing) patch_workforcemanagement_users_workplanbidranks_bulk(body)


Update bulk work plan bid ranks on users. Max 50 users can be updated at a time.

Wraps PATCH /api/v2/workforcemanagement/users/workplanbidranks/bulk 

Requires ANY permissions: 

* wfm:workPlanBid:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = [PureCloudPlatformClientV2.WorkPlanBidRanks()] # list[WorkPlanBidRanks] | Users

try:
    # Update bulk work plan bid ranks on users. Max 50 users can be updated at a time.
    api_response = api_instance.patch_workforcemanagement_users_workplanbidranks_bulk(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_users_workplanbidranks_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**list[WorkPlanBidRanks]**](WorkPlanBidRanks)| Users |  |

### Return type

[**EntityListing**](EntityListing)


## patch_workforcemanagement_workplanbid_preferences

> [**AgentWorkPlanBiddingPreferenceResponse**](AgentWorkPlanBiddingPreferenceResponse) patch_workforcemanagement_workplanbid_preferences(bid_id, body=body)


Update an agent's work plan bidding preference

Wraps PATCH /api/v2/workforcemanagement/workplanbids/{bidId}/preferences 

Requires ANY permissions: 

* wfm:agentWorkPlanBid:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
bid_id = 'bid_id_example' # str | The ID of the work plan bid
body = PureCloudPlatformClientV2.UpdateAgentWorkPlanBiddingPreference() # UpdateAgentWorkPlanBiddingPreference | body (optional)

try:
    # Update an agent's work plan bidding preference
    api_response = api_instance.patch_workforcemanagement_workplanbid_preferences(bid_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->patch_workforcemanagement_workplanbid_preferences: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **bid_id** | **str**| The ID of the work plan bid |  |
| **body** | [**UpdateAgentWorkPlanBiddingPreference**](UpdateAgentWorkPlanBiddingPreference)| body | [optional]  |

### Return type

[**AgentWorkPlanBiddingPreferenceResponse**](AgentWorkPlanBiddingPreferenceResponse)


## post_workforcemanagement_adherence_explanations

> [**AdherenceExplanationAsyncResponse**](AdherenceExplanationAsyncResponse) post_workforcemanagement_adherence_explanations(body)


Submit an adherence explanation for the current user

Wraps POST /api/v2/workforcemanagement/adherence/explanations 

Requires ANY permissions: 

* wfm:agentAdherenceExplanation:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.AddAdherenceExplanationAgentRequest() # AddAdherenceExplanationAgentRequest | The request body

try:
    # Submit an adherence explanation for the current user
    api_response = api_instance.post_workforcemanagement_adherence_explanations(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_adherence_explanations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AddAdherenceExplanationAgentRequest**](AddAdherenceExplanationAgentRequest)| The request body |  |

### Return type

[**AdherenceExplanationAsyncResponse**](AdherenceExplanationAsyncResponse)


## post_workforcemanagement_adherence_explanations_query

> [**QueryAdherenceExplanationsResponse**](QueryAdherenceExplanationsResponse) post_workforcemanagement_adherence_explanations_query(body, force_async=force_async, force_download_service=force_download_service)


Query adherence explanations for the current user

Wraps POST /api/v2/workforcemanagement/adherence/explanations/query 

Requires ANY permissions: 

* wfm:agentAdherenceExplanation:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.AgentQueryAdherenceExplanationsRequest() # AgentQueryAdherenceExplanationsRequest | The request body
force_async = True # bool | Force the result of this operation to be sent asynchronously via notification. For testing/app development purposes (optional)
force_download_service = True # bool | Force the result of this operation to be sent via download service. For testing/app development purposes (optional)

try:
    # Query adherence explanations for the current user
    api_response = api_instance.post_workforcemanagement_adherence_explanations_query(body, force_async=force_async, force_download_service=force_download_service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_adherence_explanations_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AgentQueryAdherenceExplanationsRequest**](AgentQueryAdherenceExplanationsRequest)| The request body |  |
| **force_async** | **bool**| Force the result of this operation to be sent asynchronously via notification. For testing/app development purposes | [optional]  |
| **force_download_service** | **bool**| Force the result of this operation to be sent via download service. For testing/app development purposes | [optional]  |

### Return type

[**QueryAdherenceExplanationsResponse**](QueryAdherenceExplanationsResponse)


## post_workforcemanagement_adherence_historical

> [**WfmHistoricalAdherenceResponse**](WfmHistoricalAdherenceResponse) post_workforcemanagement_adherence_historical(body=body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Deprecated. Use bulk routes instead (/adherence/historical/bulk)

Wraps POST /api/v2/workforcemanagement/adherence/historical 

Requires ANY permissions: 

* wfm:historicalAdherence:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.WfmHistoricalAdherenceQueryForUsers() # WfmHistoricalAdherenceQueryForUsers | body (optional)

try:
    # Deprecated. Use bulk routes instead (/adherence/historical/bulk)
    api_response = api_instance.post_workforcemanagement_adherence_historical(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_adherence_historical: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WfmHistoricalAdherenceQueryForUsers**](WfmHistoricalAdherenceQueryForUsers)| body | [optional]  |

### Return type

[**WfmHistoricalAdherenceResponse**](WfmHistoricalAdherenceResponse)


## post_workforcemanagement_adherence_historical_bulk

> [**WfmHistoricalAdherenceBulkResponse**](WfmHistoricalAdherenceBulkResponse) post_workforcemanagement_adherence_historical_bulk(body=body)


Request a historical adherence report in bulk

Wraps POST /api/v2/workforcemanagement/adherence/historical/bulk 

Requires ANY permissions: 

* wfm:historicalAdherence:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.WfmHistoricalAdherenceBulkQuery() # WfmHistoricalAdherenceBulkQuery | body (optional)

try:
    # Request a historical adherence report in bulk
    api_response = api_instance.post_workforcemanagement_adherence_historical_bulk(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_adherence_historical_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**WfmHistoricalAdherenceBulkQuery**](WfmHistoricalAdherenceBulkQuery)| body | [optional]  |

### Return type

[**WfmHistoricalAdherenceBulkResponse**](WfmHistoricalAdherenceBulkResponse)


## post_workforcemanagement_agent_adherence_explanations

> [**AdherenceExplanationAsyncResponse**](AdherenceExplanationAsyncResponse) post_workforcemanagement_agent_adherence_explanations(agent_id, body)


Add an adherence explanation for the requested user

Wraps POST /api/v2/workforcemanagement/agents/{agentId}/adherence/explanations 

Requires ANY permissions: 

* wfm:adherenceExplanation:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
agent_id = 'agent_id_example' # str | The ID of the agent to query
body = PureCloudPlatformClientV2.AddAdherenceExplanationAdminRequest() # AddAdherenceExplanationAdminRequest | The request body

try:
    # Add an adherence explanation for the requested user
    api_response = api_instance.post_workforcemanagement_agent_adherence_explanations(agent_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_agent_adherence_explanations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str**| The ID of the agent to query |  |
| **body** | [**AddAdherenceExplanationAdminRequest**](AddAdherenceExplanationAdminRequest)| The request body |  |

### Return type

[**AdherenceExplanationAsyncResponse**](AdherenceExplanationAsyncResponse)


## post_workforcemanagement_agent_adherence_explanations_query

> [**AgentQueryAdherenceExplanationsResponse**](AgentQueryAdherenceExplanationsResponse) post_workforcemanagement_agent_adherence_explanations_query(agent_id, body, force_async=force_async, force_download_service=force_download_service)


Query adherence explanations for the given agent across a specified range

Wraps POST /api/v2/workforcemanagement/agents/{agentId}/adherence/explanations/query 

Requires ANY permissions: 

* wfm:adherenceExplanation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
agent_id = 'agent_id_example' # str | The ID of the agent to query
body = PureCloudPlatformClientV2.AgentQueryAdherenceExplanationsRequest() # AgentQueryAdherenceExplanationsRequest | The request body
force_async = True # bool | Force the result of this operation to be sent asynchronously via notification. For testing/app development purposes (optional)
force_download_service = True # bool | Force the result of this operation to be sent via download service. For testing/app development purposes (optional)

try:
    # Query adherence explanations for the given agent across a specified range
    api_response = api_instance.post_workforcemanagement_agent_adherence_explanations_query(agent_id, body, force_async=force_async, force_download_service=force_download_service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_agent_adherence_explanations_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str**| The ID of the agent to query |  |
| **body** | [**AgentQueryAdherenceExplanationsRequest**](AgentQueryAdherenceExplanationsRequest)| The request body |  |
| **force_async** | **bool**| Force the result of this operation to be sent asynchronously via notification. For testing/app development purposes | [optional]  |
| **force_download_service** | **bool**| Force the result of this operation to be sent via download service. For testing/app development purposes | [optional]  |

### Return type

[**AgentQueryAdherenceExplanationsResponse**](AgentQueryAdherenceExplanationsResponse)


## post_workforcemanagement_agents

> [**MoveAgentsResponse**](MoveAgentsResponse) post_workforcemanagement_agents(body=body)


Move agents in and out of management unit

Wraps POST /api/v2/workforcemanagement/agents 

Requires ANY permissions: 

* wfm:agent:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.MoveAgentsRequest() # MoveAgentsRequest | body (optional)

try:
    # Move agents in and out of management unit
    api_response = api_instance.post_workforcemanagement_agents(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_agents: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**MoveAgentsRequest**](MoveAgentsRequest)| body | [optional]  |

### Return type

[**MoveAgentsResponse**](MoveAgentsResponse)


## post_workforcemanagement_agents_integrations_hris_query

> [**AgentsIntegrationsListing**](AgentsIntegrationsListing) post_workforcemanagement_agents_integrations_hris_query(body=body)


Query integrations for agents

Wraps POST /api/v2/workforcemanagement/agents/integrations/hris/query 

Requires ANY permissions: 

* wfm:agent:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.QueryAgentsIntegrationsRequest() # QueryAgentsIntegrationsRequest | body (optional)

try:
    # Query integrations for agents
    api_response = api_instance.post_workforcemanagement_agents_integrations_hris_query(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_agents_integrations_hris_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**QueryAgentsIntegrationsRequest**](QueryAgentsIntegrationsRequest)| body | [optional]  |

### Return type

[**AgentsIntegrationsListing**](AgentsIntegrationsListing)


## post_workforcemanagement_agents_me_possibleworkshifts

> [**AgentPossibleWorkShiftsResponse**](AgentPossibleWorkShiftsResponse) post_workforcemanagement_agents_me_possibleworkshifts(body)


Get agent possible work shifts for requested time frame

Wraps POST /api/v2/workforcemanagement/agents/me/possibleworkshifts 

Requires ANY permissions: 

* wfm:agentPossibleWorkShifts:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.AgentPossibleWorkShiftsRequest() # AgentPossibleWorkShiftsRequest | body

try:
    # Get agent possible work shifts for requested time frame
    api_response = api_instance.post_workforcemanagement_agents_me_possibleworkshifts(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_agents_me_possibleworkshifts: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AgentPossibleWorkShiftsRequest**](AgentPossibleWorkShiftsRequest)| body |  |

### Return type

[**AgentPossibleWorkShiftsResponse**](AgentPossibleWorkShiftsResponse)


## post_workforcemanagement_agentschedules_mine

> [**BuCurrentAgentScheduleSearchResponse**](BuCurrentAgentScheduleSearchResponse) post_workforcemanagement_agentschedules_mine(body=body)


Get published schedule for the current user

Wraps POST /api/v2/workforcemanagement/agentschedules/mine 

Requires ANY permissions: 

* wfm:agentSchedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.BuGetCurrentAgentScheduleRequest() # BuGetCurrentAgentScheduleRequest | body (optional)

try:
    # Get published schedule for the current user
    api_response = api_instance.post_workforcemanagement_agentschedules_mine(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_agentschedules_mine: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**BuGetCurrentAgentScheduleRequest**](BuGetCurrentAgentScheduleRequest)| body | [optional]  |

### Return type

[**BuCurrentAgentScheduleSearchResponse**](BuCurrentAgentScheduleSearchResponse)


## post_workforcemanagement_alternativeshifts_offers_jobs

> [**AlternativeShiftAsyncResponse**](AlternativeShiftAsyncResponse) post_workforcemanagement_alternativeshifts_offers_jobs(body)


Request a list of alternative shift offers for a given schedule

Wraps POST /api/v2/workforcemanagement/alternativeshifts/offers/jobs 

Requires ANY permissions: 

* wfm:agentAlternativeShift:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.AlternativeShiftOffersRequest() # AlternativeShiftOffersRequest | The request body

try:
    # Request a list of alternative shift offers for a given schedule
    api_response = api_instance.post_workforcemanagement_alternativeshifts_offers_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_alternativeshifts_offers_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AlternativeShiftOffersRequest**](AlternativeShiftOffersRequest)| The request body |  |

### Return type

[**AlternativeShiftAsyncResponse**](AlternativeShiftAsyncResponse)


## post_workforcemanagement_alternativeshifts_offers_search_jobs

> [**AlternativeShiftAsyncResponse**](AlternativeShiftAsyncResponse) post_workforcemanagement_alternativeshifts_offers_search_jobs(body)


Request a search of alternative shift offers for a given shift

Wraps POST /api/v2/workforcemanagement/alternativeshifts/offers/search/jobs 

Requires ANY permissions: 

* wfm:agentAlternativeShift:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.AlternativeShiftSearchOffersRequest() # AlternativeShiftSearchOffersRequest | The request body

try:
    # Request a search of alternative shift offers for a given shift
    api_response = api_instance.post_workforcemanagement_alternativeshifts_offers_search_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_alternativeshifts_offers_search_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AlternativeShiftSearchOffersRequest**](AlternativeShiftSearchOffersRequest)| The request body |  |

### Return type

[**AlternativeShiftAsyncResponse**](AlternativeShiftAsyncResponse)


## post_workforcemanagement_alternativeshifts_trades

> [**AlternativeShiftTradeResponse**](AlternativeShiftTradeResponse) post_workforcemanagement_alternativeshifts_trades(body)


Create my alternative shift trade using an existing offer's jobId

Wraps POST /api/v2/workforcemanagement/alternativeshifts/trades 

Requires ANY permissions: 

* wfm:agentAlternativeShift:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.CreateAlternativeShiftTradeRequest() # CreateAlternativeShiftTradeRequest | The request body

try:
    # Create my alternative shift trade using an existing offer's jobId
    api_response = api_instance.post_workforcemanagement_alternativeshifts_trades(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_alternativeshifts_trades: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateAlternativeShiftTradeRequest**](CreateAlternativeShiftTradeRequest)| The request body |  |

### Return type

[**AlternativeShiftTradeResponse**](AlternativeShiftTradeResponse)


## post_workforcemanagement_businessunit_activitycodes

> [**BusinessUnitActivityCode**](BusinessUnitActivityCode) post_workforcemanagement_businessunit_activitycodes(business_unit_id, body=body)


Create a new activity code

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/activitycodes 

Requires ANY permissions: 

* wfm:activityCode:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit, or 'mine' for the business unit of the logged-in user.
body = PureCloudPlatformClientV2.CreateActivityCodeRequest() # CreateActivityCodeRequest | body (optional)

try:
    # Create a new activity code
    api_response = api_instance.post_workforcemanagement_businessunit_activitycodes(business_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_activitycodes: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit, or &#39;mine&#39; for the business unit of the logged-in user. |  |
| **body** | [**CreateActivityCodeRequest**](CreateActivityCodeRequest)| body | [optional]  |

### Return type

[**BusinessUnitActivityCode**](BusinessUnitActivityCode)


## post_workforcemanagement_businessunit_activityplan_runs_jobs

> [**ActivityPlanJobResponse**](ActivityPlanJobResponse) post_workforcemanagement_businessunit_activityplan_runs_jobs(business_unit_id, activity_plan_id)


Run an activity plan manually

Triggers a job running the activity plan. The activity plan cannot be updated until the job completes

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/activityplans/{activityPlanId}/runs/jobs 

Requires ANY permissions: 

* wfm:activityPlanRunJob:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
activity_plan_id = 'activity_plan_id_example' # str | The ID of the activity plan to run

try:
    # Run an activity plan manually
    api_response = api_instance.post_workforcemanagement_businessunit_activityplan_runs_jobs(business_unit_id, activity_plan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_activityplan_runs_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **activity_plan_id** | **str**| The ID of the activity plan to run |  |

### Return type

[**ActivityPlanJobResponse**](ActivityPlanJobResponse)


## post_workforcemanagement_businessunit_activityplans

> [**ActivityPlanResponse**](ActivityPlanResponse) post_workforcemanagement_businessunit_activityplans(business_unit_id, body)


Create an activity plan

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/activityplans 

Requires ANY permissions: 

* wfm:activityPlan:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
body = PureCloudPlatformClientV2.CreateActivityPlanRequest() # CreateActivityPlanRequest | body

try:
    # Create an activity plan
    api_response = api_instance.post_workforcemanagement_businessunit_activityplans(business_unit_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_activityplans: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **body** | [**CreateActivityPlanRequest**](CreateActivityPlanRequest)| body |  |

### Return type

[**ActivityPlanResponse**](ActivityPlanResponse)


## post_workforcemanagement_businessunit_adherence_explanations_query

> [**BuQueryAdherenceExplanationsResponse**](BuQueryAdherenceExplanationsResponse) post_workforcemanagement_businessunit_adherence_explanations_query(business_unit_id, body, force_async=force_async, force_download_service=force_download_service)


Query adherence explanations across an entire business unit for the requested period

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/adherence/explanations/query 

Requires ANY permissions: 

* wfm:adherenceExplanation:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
body = PureCloudPlatformClientV2.BuQueryAdherenceExplanationsRequest() # BuQueryAdherenceExplanationsRequest | The request body
force_async = True # bool | Force the result of this operation to be sent asynchronously via notification. For testing/app development purposes (optional)
force_download_service = True # bool | Force the result of this operation to be sent via download service. For testing/app development purposes (optional)

try:
    # Query adherence explanations across an entire business unit for the requested period
    api_response = api_instance.post_workforcemanagement_businessunit_adherence_explanations_query(business_unit_id, body, force_async=force_async, force_download_service=force_download_service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_adherence_explanations_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **body** | [**BuQueryAdherenceExplanationsRequest**](BuQueryAdherenceExplanationsRequest)| The request body |  |
| **force_async** | **bool**| Force the result of this operation to be sent asynchronously via notification. For testing/app development purposes | [optional]  |
| **force_download_service** | **bool**| Force the result of this operation to be sent via download service. For testing/app development purposes | [optional]  |

### Return type

[**BuQueryAdherenceExplanationsResponse**](BuQueryAdherenceExplanationsResponse)


## post_workforcemanagement_businessunit_agentschedules_search

> [**BuAsyncAgentSchedulesSearchResponse**](BuAsyncAgentSchedulesSearchResponse) post_workforcemanagement_businessunit_agentschedules_search(business_unit_id, force_async=force_async, force_download_service=force_download_service, body=body)


Search published schedules

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/agentschedules/search 

Requires ANY permissions: 

* wfm:schedule:view
* wfm:publishedSchedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
force_async = True # bool | Force the result of this operation to be sent asynchronously via notification. For testing/app development purposes (optional)
force_download_service = True # bool | Force the result of this operation to be sent via download service. For testing/app development purposes (optional)
body = PureCloudPlatformClientV2.BuSearchAgentSchedulesRequest() # BuSearchAgentSchedulesRequest | body (optional)

try:
    # Search published schedules
    api_response = api_instance.post_workforcemanagement_businessunit_agentschedules_search(business_unit_id, force_async=force_async, force_download_service=force_download_service, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_agentschedules_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **force_async** | **bool**| Force the result of this operation to be sent asynchronously via notification. For testing/app development purposes | [optional]  |
| **force_download_service** | **bool**| Force the result of this operation to be sent via download service. For testing/app development purposes | [optional]  |
| **body** | [**BuSearchAgentSchedulesRequest**](BuSearchAgentSchedulesRequest)| body | [optional]  |

### Return type

[**BuAsyncAgentSchedulesSearchResponse**](BuAsyncAgentSchedulesSearchResponse)


## post_workforcemanagement_businessunit_alternativeshifts_trades_search

> [**BuListAlternativeShiftTradesResponse**](BuListAlternativeShiftTradesResponse) post_workforcemanagement_businessunit_alternativeshifts_trades_search(business_unit_id, body, force_async=force_async)


List alternative shifts trades for a given management unit or agent

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/alternativeshifts/trades/search 

Requires ANY permissions: 

* wfm:alternativeShift:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
body = PureCloudPlatformClientV2.SearchAlternativeShiftTradesRequest() # SearchAlternativeShiftTradesRequest | The request body
force_async = True # bool | Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes (optional)

try:
    # List alternative shifts trades for a given management unit or agent
    api_response = api_instance.post_workforcemanagement_businessunit_alternativeshifts_trades_search(business_unit_id, body, force_async=force_async)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_alternativeshifts_trades_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **body** | [**SearchAlternativeShiftTradesRequest**](SearchAlternativeShiftTradesRequest)| The request body |  |
| **force_async** | **bool**| Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes | [optional]  |

### Return type

[**BuListAlternativeShiftTradesResponse**](BuListAlternativeShiftTradesResponse)


## post_workforcemanagement_businessunit_intraday

> [**AsyncIntradayResponse**](AsyncIntradayResponse) post_workforcemanagement_businessunit_intraday(business_unit_id, force_async=force_async, body=body)


Get intraday data for the given date for the requested planningGroupIds

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/intraday 

Requires ANY permissions: 

* wfm:intraday:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
force_async = True # bool | Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes (optional)
body = PureCloudPlatformClientV2.IntradayPlanningGroupRequest() # IntradayPlanningGroupRequest | body (optional)

try:
    # Get intraday data for the given date for the requested planningGroupIds
    api_response = api_instance.post_workforcemanagement_businessunit_intraday(business_unit_id, force_async=force_async, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_intraday: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **force_async** | **bool**| Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes | [optional]  |
| **body** | [**IntradayPlanningGroupRequest**](IntradayPlanningGroupRequest)| body | [optional]  |

### Return type

[**AsyncIntradayResponse**](AsyncIntradayResponse)


## post_workforcemanagement_businessunit_planninggroups

> [**PlanningGroup**](PlanningGroup) post_workforcemanagement_businessunit_planninggroups(business_unit_id, body=body)


Adds a new planning group

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/planninggroups 

Requires ANY permissions: 

* wfm:planningGroup:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit.
body = PureCloudPlatformClientV2.CreatePlanningGroupRequest() # CreatePlanningGroupRequest | body (optional)

try:
    # Adds a new planning group
    api_response = api_instance.post_workforcemanagement_businessunit_planninggroups(business_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_planninggroups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit. |  |
| **body** | [**CreatePlanningGroupRequest**](CreatePlanningGroupRequest)| body | [optional]  |

### Return type

[**PlanningGroup**](PlanningGroup)


## post_workforcemanagement_businessunit_servicegoaltemplates

> [**ServiceGoalTemplate**](ServiceGoalTemplate) post_workforcemanagement_businessunit_servicegoaltemplates(business_unit_id, body=body)


Adds a new service goal template

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/servicegoaltemplates 

Requires ANY permissions: 

* wfm:serviceGoalTemplate:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit.
body = PureCloudPlatformClientV2.CreateServiceGoalTemplate() # CreateServiceGoalTemplate | body (optional)

try:
    # Adds a new service goal template
    api_response = api_instance.post_workforcemanagement_businessunit_servicegoaltemplates(business_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_servicegoaltemplates: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit. |  |
| **body** | [**CreateServiceGoalTemplate**](CreateServiceGoalTemplate)| body | [optional]  |

### Return type

[**ServiceGoalTemplate**](ServiceGoalTemplate)


## post_workforcemanagement_businessunit_staffinggroups

> [**StaffingGroupResponse**](StaffingGroupResponse) post_workforcemanagement_businessunit_staffinggroups(business_unit_id, body=body)


Creates a new staffing group

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/staffinggroups 

Requires ANY permissions: 

* wfm:staffingGroup:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
body = PureCloudPlatformClientV2.CreateStaffingGroupRequest() # CreateStaffingGroupRequest | body (optional)

try:
    # Creates a new staffing group
    api_response = api_instance.post_workforcemanagement_businessunit_staffinggroups(business_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_staffinggroups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **body** | [**CreateStaffingGroupRequest**](CreateStaffingGroupRequest)| body | [optional]  |

### Return type

[**StaffingGroupResponse**](StaffingGroupResponse)


## post_workforcemanagement_businessunit_staffinggroups_query

> [**UserStaffingGroupListing**](UserStaffingGroupListing) post_workforcemanagement_businessunit_staffinggroups_query(business_unit_id, body=body)


Gets staffing group associations for a list of user IDs

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/staffinggroups/query 

Requires ANY permissions: 

* wfm:staffingGroup:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
body = PureCloudPlatformClientV2.QueryUserStaffingGroupListRequest() # QueryUserStaffingGroupListRequest | body (optional)

try:
    # Gets staffing group associations for a list of user IDs
    api_response = api_instance.post_workforcemanagement_businessunit_staffinggroups_query(business_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_staffinggroups_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **body** | [**QueryUserStaffingGroupListRequest**](QueryUserStaffingGroupListRequest)| body | [optional]  |

### Return type

[**UserStaffingGroupListing**](UserStaffingGroupListing)


## post_workforcemanagement_businessunit_timeofflimits

> [**BuTimeOffLimitResponse**](BuTimeOffLimitResponse) post_workforcemanagement_businessunit_timeofflimits(business_unit_id, body=body)


Creates a new time-off limit object

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/timeofflimits 

Requires ANY permissions: 

* wfm:timeOffLimit:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
body = PureCloudPlatformClientV2.BuCreateTimeOffLimitRequest() # BuCreateTimeOffLimitRequest | body (optional)

try:
    # Creates a new time-off limit object
    api_response = api_instance.post_workforcemanagement_businessunit_timeofflimits(business_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_timeofflimits: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **body** | [**BuCreateTimeOffLimitRequest**](BuCreateTimeOffLimitRequest)| body | [optional]  |

### Return type

[**BuTimeOffLimitResponse**](BuTimeOffLimitResponse)


## post_workforcemanagement_businessunit_timeofflimits_values_query

> [**BuTimeOffLimitValuesResponse**](BuTimeOffLimitValuesResponse) post_workforcemanagement_businessunit_timeofflimits_values_query(business_unit_id, body=body)


Retrieves time-off limit related values based on a given set of filters.

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/timeofflimits/values/query 

Requires ANY permissions: 

* wfm:timeOffLimit:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
body = PureCloudPlatformClientV2.QueryTimeOffLimitValuesRequest() # QueryTimeOffLimitValuesRequest | body (optional)

try:
    # Retrieves time-off limit related values based on a given set of filters.
    api_response = api_instance.post_workforcemanagement_businessunit_timeofflimits_values_query(business_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_timeofflimits_values_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **body** | [**QueryTimeOffLimitValuesRequest**](QueryTimeOffLimitValuesRequest)| body | [optional]  |

### Return type

[**BuTimeOffLimitValuesResponse**](BuTimeOffLimitValuesResponse)


## post_workforcemanagement_businessunit_timeoffplans

> [**BuTimeOffPlanResponse**](BuTimeOffPlanResponse) post_workforcemanagement_businessunit_timeoffplans(business_unit_id, body=body)


Creates a new time-off plan

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/timeoffplans 

Requires ANY permissions: 

* wfm:timeOffPlan:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
body = PureCloudPlatformClientV2.BuCreateTimeOffPlanRequest() # BuCreateTimeOffPlanRequest | body (optional)

try:
    # Creates a new time-off plan
    api_response = api_instance.post_workforcemanagement_businessunit_timeoffplans(business_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_timeoffplans: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **body** | [**BuCreateTimeOffPlanRequest**](BuCreateTimeOffPlanRequest)| body | [optional]  |

### Return type

[**BuTimeOffPlanResponse**](BuTimeOffPlanResponse)


## post_workforcemanagement_businessunit_week_schedule_agentschedules_query

> [**BuAsyncAgentSchedulesQueryResponse**](BuAsyncAgentSchedulesQueryResponse) post_workforcemanagement_businessunit_week_schedule_agentschedules_query(business_unit_id, week_id, schedule_id, body, force_async=force_async, force_download_service=force_download_service)


Loads agent schedule data from the schedule. Used in combination with the metadata route

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId}/agentschedules/query 

Requires ANY permissions: 

* wfm:schedule:view
* wfm:publishedSchedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
week_id = '2013-10-20' # date | First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
schedule_id = 'schedule_id_example' # str | The ID of the schedule
body = PureCloudPlatformClientV2.BuQueryAgentSchedulesRequest() # BuQueryAgentSchedulesRequest | body
force_async = True # bool | Force the result of this operation to be sent asynchronously via notification. For testing/app development purposes (optional)
force_download_service = True # bool | Force the result of this operation to be sent via download service. For testing/app development purposes (optional)

try:
    # Loads agent schedule data from the schedule. Used in combination with the metadata route
    api_response = api_instance.post_workforcemanagement_businessunit_week_schedule_agentschedules_query(business_unit_id, week_id, schedule_id, body, force_async=force_async, force_download_service=force_download_service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_week_schedule_agentschedules_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **week_id** | **date**| First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **schedule_id** | **str**| The ID of the schedule |  |
| **body** | [**BuQueryAgentSchedulesRequest**](BuQueryAgentSchedulesRequest)| body |  |
| **force_async** | **bool**| Force the result of this operation to be sent asynchronously via notification. For testing/app development purposes | [optional]  |
| **force_download_service** | **bool**| Force the result of this operation to be sent via download service. For testing/app development purposes | [optional]  |

### Return type

[**BuAsyncAgentSchedulesQueryResponse**](BuAsyncAgentSchedulesQueryResponse)


## post_workforcemanagement_businessunit_week_schedule_copy

> [**BuAsyncScheduleResponse**](BuAsyncScheduleResponse) post_workforcemanagement_businessunit_week_schedule_copy(business_unit_id, week_id, schedule_id, body)


Copy a schedule

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId}/copy 

Requires ANY permissions: 

* wfm:schedule:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
week_id = '2013-10-20' # date | First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
schedule_id = 'schedule_id_example' # str | The ID of the schedule to copy
body = PureCloudPlatformClientV2.BuCopyScheduleRequest() # BuCopyScheduleRequest | body

try:
    # Copy a schedule
    api_response = api_instance.post_workforcemanagement_businessunit_week_schedule_copy(business_unit_id, week_id, schedule_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_week_schedule_copy: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **week_id** | **date**| First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **schedule_id** | **str**| The ID of the schedule to copy |  |
| **body** | [**BuCopyScheduleRequest**](BuCopyScheduleRequest)| body |  |

### Return type

[**BuAsyncScheduleResponse**](BuAsyncScheduleResponse)


## post_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculations

> [**PerformancePredictionRecalculationResponse**](PerformancePredictionRecalculationResponse) post_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculations(business_unit_id, week_id, schedule_id, body=body)


Request a daily recalculation of the performance prediction for the associated schedule

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId}/performancepredictions/recalculations 

Requires ANY permissions: 

* wfm:schedule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit to which the performance prediction belongs
week_id = 'week_id_example' # str | First day of schedule week in yyyy-MM-dd format
schedule_id = 'schedule_id_example' # str | The ID of the schedule the performance prediction belongs to
body = PureCloudPlatformClientV2.WfmProcessUploadRequest() # WfmProcessUploadRequest | body (optional)

try:
    # Request a daily recalculation of the performance prediction for the associated schedule
    api_response = api_instance.post_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculations(business_unit_id, week_id, schedule_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit to which the performance prediction belongs |  |
| **week_id** | **str**| First day of schedule week in yyyy-MM-dd format |  |
| **schedule_id** | **str**| The ID of the schedule the performance prediction belongs to |  |
| **body** | [**WfmProcessUploadRequest**](WfmProcessUploadRequest)| body | [optional]  |

### Return type

[**PerformancePredictionRecalculationResponse**](PerformancePredictionRecalculationResponse)


## post_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculations_uploadurl

> [**PerformancePredictionRecalculationUploadResponse**](PerformancePredictionRecalculationUploadResponse) post_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculations_uploadurl(business_unit_id, week_id, schedule_id, body=body)


Upload daily activity changes to be able to request a performance prediction recalculation

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId}/performancepredictions/recalculations/uploadurl 

Requires ANY permissions: 

* wfm:schedule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit to which the performance prediction belongs
week_id = 'week_id_example' # str | First day of schedule week in yyyy-MM-dd format
schedule_id = 'schedule_id_example' # str | The ID of the schedule the performance prediction belongs to
body = PureCloudPlatformClientV2.UploadUrlRequestBody() # UploadUrlRequestBody | body (optional)

try:
    # Upload daily activity changes to be able to request a performance prediction recalculation
    api_response = api_instance.post_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculations_uploadurl(business_unit_id, week_id, schedule_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_week_schedule_performancepredictions_recalculations_uploadurl: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit to which the performance prediction belongs |  |
| **week_id** | **str**| First day of schedule week in yyyy-MM-dd format |  |
| **schedule_id** | **str**| The ID of the schedule the performance prediction belongs to |  |
| **body** | [**UploadUrlRequestBody**](UploadUrlRequestBody)| body | [optional]  |

### Return type

[**PerformancePredictionRecalculationUploadResponse**](PerformancePredictionRecalculationUploadResponse)


## post_workforcemanagement_businessunit_week_schedule_reschedule

> [**BuAsyncScheduleRunResponse**](BuAsyncScheduleRunResponse) post_workforcemanagement_businessunit_week_schedule_reschedule(business_unit_id, week_id, schedule_id, body)


Start a rescheduling run

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId}/reschedule 

Requires ANY permissions: 

* wfm:schedule:generate

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
week_id = '2013-10-20' # date | First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
schedule_id = 'schedule_id_example' # str | The ID of the schedule
body = PureCloudPlatformClientV2.BuRescheduleRequest() # BuRescheduleRequest | body

try:
    # Start a rescheduling run
    api_response = api_instance.post_workforcemanagement_businessunit_week_schedule_reschedule(business_unit_id, week_id, schedule_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_week_schedule_reschedule: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **week_id** | **date**| First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **schedule_id** | **str**| The ID of the schedule |  |
| **body** | [**BuRescheduleRequest**](BuRescheduleRequest)| body |  |

### Return type

[**BuAsyncScheduleRunResponse**](BuAsyncScheduleRunResponse)


## post_workforcemanagement_businessunit_week_schedule_update

> [**BuAsyncScheduleResponse**](BuAsyncScheduleResponse) post_workforcemanagement_businessunit_week_schedule_update(business_unit_id, week_id, schedule_id, body)


Starts processing a schedule update

Call after uploading the schedule data to the url supplied by the /update/uploadurl route

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId}/update 

Requires ANY permissions: 

* wfm:schedule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
week_id = '2013-10-20' # date | First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
schedule_id = 'schedule_id_example' # str | The ID of the schedule
body = PureCloudPlatformClientV2.ProcessScheduleUpdateUploadRequest() # ProcessScheduleUpdateUploadRequest | body

try:
    # Starts processing a schedule update
    api_response = api_instance.post_workforcemanagement_businessunit_week_schedule_update(business_unit_id, week_id, schedule_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_week_schedule_update: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **week_id** | **date**| First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **schedule_id** | **str**| The ID of the schedule |  |
| **body** | [**ProcessScheduleUpdateUploadRequest**](ProcessScheduleUpdateUploadRequest)| body |  |

### Return type

[**BuAsyncScheduleResponse**](BuAsyncScheduleResponse)


## post_workforcemanagement_businessunit_week_schedule_update_uploadurl

> [**UpdateScheduleUploadResponse**](UpdateScheduleUploadResponse) post_workforcemanagement_businessunit_week_schedule_update_uploadurl(business_unit_id, week_id, schedule_id, body)


Creates a signed upload URL for updating a schedule

Once the upload is complete, call the /{scheduleId}/update route to start the schedule update process

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/{scheduleId}/update/uploadurl 

Requires ANY permissions: 

* wfm:schedule:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
week_id = '2013-10-20' # date | First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
schedule_id = 'schedule_id_example' # str | The ID of the schedule
body = PureCloudPlatformClientV2.UploadUrlRequestBody() # UploadUrlRequestBody | body

try:
    # Creates a signed upload URL for updating a schedule
    api_response = api_instance.post_workforcemanagement_businessunit_week_schedule_update_uploadurl(business_unit_id, week_id, schedule_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_week_schedule_update_uploadurl: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **week_id** | **date**| First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **schedule_id** | **str**| The ID of the schedule |  |
| **body** | [**UploadUrlRequestBody**](UploadUrlRequestBody)| body |  |

### Return type

[**UpdateScheduleUploadResponse**](UpdateScheduleUploadResponse)


## post_workforcemanagement_businessunit_week_schedules

> [**BuScheduleMetadata**](BuScheduleMetadata) post_workforcemanagement_businessunit_week_schedules(business_unit_id, week_id, body)


Create a blank schedule

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules 

Requires ANY permissions: 

* wfm:schedule:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
week_id = '2013-10-20' # date | First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
body = PureCloudPlatformClientV2.BuCreateBlankScheduleRequest() # BuCreateBlankScheduleRequest | body

try:
    # Create a blank schedule
    api_response = api_instance.post_workforcemanagement_businessunit_week_schedules(business_unit_id, week_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_week_schedules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **week_id** | **date**| First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **body** | [**BuCreateBlankScheduleRequest**](BuCreateBlankScheduleRequest)| body |  |

### Return type

[**BuScheduleMetadata**](BuScheduleMetadata)


## post_workforcemanagement_businessunit_week_schedules_generate

> [**BuAsyncScheduleRunResponse**](BuAsyncScheduleRunResponse) post_workforcemanagement_businessunit_week_schedules_generate(business_unit_id, week_id, body)


Generate a schedule

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/generate 

Requires ANY permissions: 

* wfm:schedule:generate

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
week_id = '2013-10-20' # date | First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
body = PureCloudPlatformClientV2.BuGenerateScheduleRequest() # BuGenerateScheduleRequest | body

try:
    # Generate a schedule
    api_response = api_instance.post_workforcemanagement_businessunit_week_schedules_generate(business_unit_id, week_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_week_schedules_generate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **week_id** | **date**| First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **body** | [**BuGenerateScheduleRequest**](BuGenerateScheduleRequest)| body |  |

### Return type

[**BuAsyncScheduleRunResponse**](BuAsyncScheduleRunResponse)


## post_workforcemanagement_businessunit_week_schedules_import

> [**ScheduleUploadProcessingResponse**](ScheduleUploadProcessingResponse) post_workforcemanagement_businessunit_week_schedules_import(business_unit_id, week_id, body)


Starts processing a schedule import

Call after uploading the schedule data to the url supplied by the /import/uploadurl route

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/import 

Requires ANY permissions: 

* wfm:schedule:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
week_id = '2013-10-20' # date | First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
body = PureCloudPlatformClientV2.WfmProcessUploadRequest() # WfmProcessUploadRequest | 

try:
    # Starts processing a schedule import
    api_response = api_instance.post_workforcemanagement_businessunit_week_schedules_import(business_unit_id, week_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_week_schedules_import: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **week_id** | **date**| First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **body** | [**WfmProcessUploadRequest**](WfmProcessUploadRequest)|  |  |

### Return type

[**ScheduleUploadProcessingResponse**](ScheduleUploadProcessingResponse)


## post_workforcemanagement_businessunit_week_schedules_import_uploadurl

> [**ImportScheduleUploadResponse**](ImportScheduleUploadResponse) post_workforcemanagement_businessunit_week_schedules_import_uploadurl(business_unit_id, week_id, body)


Creates a signed upload URL for importing a schedule

Once the upload is complete, call the /import route to start the schedule import process

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekId}/schedules/import/uploadurl 

Requires ANY permissions: 

* wfm:schedule:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
week_id = '2013-10-20' # date | First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
body = PureCloudPlatformClientV2.UploadUrlRequestBody() # UploadUrlRequestBody | body

try:
    # Creates a signed upload URL for importing a schedule
    api_response = api_instance.post_workforcemanagement_businessunit_week_schedules_import_uploadurl(business_unit_id, week_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_week_schedules_import_uploadurl: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **week_id** | **date**| First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **body** | [**UploadUrlRequestBody**](UploadUrlRequestBody)| body |  |

### Return type

[**ImportScheduleUploadResponse**](ImportScheduleUploadResponse)


## post_workforcemanagement_businessunit_week_shorttermforecast_copy

> [**AsyncForecastOperationResult**](AsyncForecastOperationResult) post_workforcemanagement_businessunit_week_shorttermforecast_copy(business_unit_id, week_date_id, forecast_id, body, force_async=force_async)


Copy a short term forecast

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekDateId}/shorttermforecasts/{forecastId}/copy 

Requires ANY permissions: 

* wfm:shortTermForecast:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit to which the forecast belongs
week_date_id = '2013-10-20' # date | The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
forecast_id = 'forecast_id_example' # str | The ID of the forecast to copy
body = PureCloudPlatformClientV2.CopyBuForecastRequest() # CopyBuForecastRequest | body
force_async = True # bool | Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes (optional)

try:
    # Copy a short term forecast
    api_response = api_instance.post_workforcemanagement_businessunit_week_shorttermforecast_copy(business_unit_id, week_date_id, forecast_id, body, force_async=force_async)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_week_shorttermforecast_copy: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit to which the forecast belongs |  |
| **week_date_id** | **date**| The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **forecast_id** | **str**| The ID of the forecast to copy |  |
| **body** | [**CopyBuForecastRequest**](CopyBuForecastRequest)| body |  |
| **force_async** | **bool**| Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes | [optional]  |

### Return type

[**AsyncForecastOperationResult**](AsyncForecastOperationResult)


## post_workforcemanagement_businessunit_week_shorttermforecasts_generate

> [**AsyncForecastOperationResult**](AsyncForecastOperationResult) post_workforcemanagement_businessunit_week_shorttermforecasts_generate(business_unit_id, week_date_id, body, force_async=force_async)


Generate a short term forecast

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekDateId}/shorttermforecasts/generate 

Requires ANY permissions: 

* wfm:shortTermForecast:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit to which the forecast belongs
week_date_id = '2013-10-20' # date | The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
body = PureCloudPlatformClientV2.GenerateBuForecastRequest() # GenerateBuForecastRequest | body
force_async = True # bool | Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes (optional)

try:
    # Generate a short term forecast
    api_response = api_instance.post_workforcemanagement_businessunit_week_shorttermforecasts_generate(business_unit_id, week_date_id, body, force_async=force_async)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_week_shorttermforecasts_generate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit to which the forecast belongs |  |
| **week_date_id** | **date**| The week start date of the forecast in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **body** | [**GenerateBuForecastRequest**](GenerateBuForecastRequest)| body |  |
| **force_async** | **bool**| Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes | [optional]  |

### Return type

[**AsyncForecastOperationResult**](AsyncForecastOperationResult)


## post_workforcemanagement_businessunit_week_shorttermforecasts_import

> [**ImportForecastResponse**](ImportForecastResponse) post_workforcemanagement_businessunit_week_shorttermforecasts_import(business_unit_id, week_date_id, body)


Starts importing the uploaded short term forecast

Call after uploading the forecast data to the url supplied by the /import/uploadurl route

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekDateId}/shorttermforecasts/import 

Requires ANY permissions: 

* wfm:shortTermForecast:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit to which the forecast belongs
week_date_id = '2013-10-20' # date | First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
body = PureCloudPlatformClientV2.WfmProcessUploadRequest() # WfmProcessUploadRequest | body

try:
    # Starts importing the uploaded short term forecast
    api_response = api_instance.post_workforcemanagement_businessunit_week_shorttermforecasts_import(business_unit_id, week_date_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_week_shorttermforecasts_import: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit to which the forecast belongs |  |
| **week_date_id** | **date**| First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **body** | [**WfmProcessUploadRequest**](WfmProcessUploadRequest)| body |  |

### Return type

[**ImportForecastResponse**](ImportForecastResponse)


## post_workforcemanagement_businessunit_week_shorttermforecasts_import_uploadurl

> [**ImportForecastUploadResponse**](ImportForecastUploadResponse) post_workforcemanagement_businessunit_week_shorttermforecasts_import_uploadurl(business_unit_id, week_date_id, body)


Creates a signed upload URL for importing a short term forecast

Once the upload is complete, call the /import route to start the short term forecast import process

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/weeks/{weekDateId}/shorttermforecasts/import/uploadurl 

Requires ANY permissions: 

* wfm:shortTermForecast:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit to which the forecast belongs
week_date_id = '2013-10-20' # date | First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
body = PureCloudPlatformClientV2.UploadUrlRequestBody() # UploadUrlRequestBody | body

try:
    # Creates a signed upload URL for importing a short term forecast
    api_response = api_instance.post_workforcemanagement_businessunit_week_shorttermforecasts_import_uploadurl(business_unit_id, week_date_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_week_shorttermforecasts_import_uploadurl: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit to which the forecast belongs |  |
| **week_date_id** | **date**| First day of schedule week in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **body** | [**UploadUrlRequestBody**](UploadUrlRequestBody)| body |  |

### Return type

[**ImportForecastUploadResponse**](ImportForecastUploadResponse)


## post_workforcemanagement_businessunit_workplanbid_copy

> [**WorkPlanBid**](WorkPlanBid) post_workforcemanagement_businessunit_workplanbid_copy(business_unit_id, bid_id, body=body)


Copy a work plan bid

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/workplanbids/{bidId}/copy 

Requires ANY permissions: 

* wfm:workPlanBid:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
bid_id = 'bid_id_example' # str | The ID of the work plan bid to copy
body = PureCloudPlatformClientV2.CopyWorkPlanBid() # CopyWorkPlanBid | body (optional)

try:
    # Copy a work plan bid
    api_response = api_instance.post_workforcemanagement_businessunit_workplanbid_copy(business_unit_id, bid_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_workplanbid_copy: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **bid_id** | **str**| The ID of the work plan bid to copy |  |
| **body** | [**CopyWorkPlanBid**](CopyWorkPlanBid)| body | [optional]  |

### Return type

[**WorkPlanBid**](WorkPlanBid)


## post_workforcemanagement_businessunit_workplanbid_groups

> [**WorkPlanBidGroupResponse**](WorkPlanBidGroupResponse) post_workforcemanagement_businessunit_workplanbid_groups(business_unit_id, bid_id, body=body)


Add a bid group in a given work plan bid

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/workplanbids/{bidId}/groups 

Requires ANY permissions: 

* wfm:workPlanBidGroup:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
bid_id = 'bid_id_example' # str | The work plan bid id of the bid groups
body = PureCloudPlatformClientV2.WorkPlanBidGroupCreate() # WorkPlanBidGroupCreate | body (optional)

try:
    # Add a bid group in a given work plan bid
    api_response = api_instance.post_workforcemanagement_businessunit_workplanbid_groups(business_unit_id, bid_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_workplanbid_groups: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **bid_id** | **str**| The work plan bid id of the bid groups |  |
| **body** | [**WorkPlanBidGroupCreate**](WorkPlanBidGroupCreate)| body | [optional]  |

### Return type

[**WorkPlanBidGroupResponse**](WorkPlanBidGroupResponse)


## post_workforcemanagement_businessunit_workplanbids

> [**WorkPlanBid**](WorkPlanBid) post_workforcemanagement_businessunit_workplanbids(business_unit_id, body=body)


Create a new work plan bid

Wraps POST /api/v2/workforcemanagement/businessunits/{businessUnitId}/workplanbids 

Requires ANY permissions: 

* wfm:workPlanBid:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
body = PureCloudPlatformClientV2.CreateWorkPlanBid() # CreateWorkPlanBid | The work plan bid to be created (optional)

try:
    # Create a new work plan bid
    api_response = api_instance.post_workforcemanagement_businessunit_workplanbids(business_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunit_workplanbids: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **body** | [**CreateWorkPlanBid**](CreateWorkPlanBid)| The work plan bid to be created | [optional]  |

### Return type

[**WorkPlanBid**](WorkPlanBid)


## post_workforcemanagement_businessunits

> [**BusinessUnitResponse**](BusinessUnitResponse) post_workforcemanagement_businessunits(body=body)


Add a new business unit

It may take a minute or two for a new business unit to be available for api operations

Wraps POST /api/v2/workforcemanagement/businessunits 

Requires ANY permissions: 

* wfm:businessUnit:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.CreateBusinessUnitRequest() # CreateBusinessUnitRequest | body (optional)

try:
    # Add a new business unit
    api_response = api_instance.post_workforcemanagement_businessunits(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_businessunits: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateBusinessUnitRequest**](CreateBusinessUnitRequest)| body | [optional]  |

### Return type

[**BusinessUnitResponse**](BusinessUnitResponse)


## post_workforcemanagement_calendar_url_ics

> [**CalendarUrlResponse**](CalendarUrlResponse) post_workforcemanagement_calendar_url_ics(language=language)


Create a newly generated calendar link for the current user; if the current user has previously generated one, the generated link will be returned

Wraps POST /api/v2/workforcemanagement/calendar/url/ics 

Requires ALL permissions: 

* wfm:agentSchedule:sync
* wfm:agentSchedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
language = ''en-US'' # str | A language tag (which is sometimes referred to as a \"locale identifier\") to use to localize default activity code names in the ics-formatted calendar (optional) (default to 'en-US')

try:
    # Create a newly generated calendar link for the current user; if the current user has previously generated one, the generated link will be returned
    api_response = api_instance.post_workforcemanagement_calendar_url_ics(language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_calendar_url_ics: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **language** | **str**| A language tag (which is sometimes referred to as a \&quot;locale identifier\&quot;) to use to localize default activity code names in the ics-formatted calendar | [optional] [default to &#39;en-US&#39;] |

### Return type

[**CalendarUrlResponse**](CalendarUrlResponse)


## post_workforcemanagement_historicaldata_bulk_remove_jobs

> [**HistoricalImportDeleteFilesJobResponse**](HistoricalImportDeleteFilesJobResponse) post_workforcemanagement_historicaldata_bulk_remove_jobs(body=body)


Delete the list of the historical data import entries

Wraps POST /api/v2/workforcemanagement/historicaldata/bulk/remove/jobs 

Requires ALL permissions: 

* wfm:historicalData:upload

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.HistoricalImportDeleteFilesJobRequest() # HistoricalImportDeleteFilesJobRequest | body (optional)

try:
    # Delete the list of the historical data import entries
    api_response = api_instance.post_workforcemanagement_historicaldata_bulk_remove_jobs(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_historicaldata_bulk_remove_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**HistoricalImportDeleteFilesJobRequest**](HistoricalImportDeleteFilesJobRequest)| body | [optional]  |

### Return type

[**HistoricalImportDeleteFilesJobResponse**](HistoricalImportDeleteFilesJobResponse)


## post_workforcemanagement_historicaldata_deletejob

> [**HistoricalImportDeleteJobResponse**](HistoricalImportDeleteJobResponse) post_workforcemanagement_historicaldata_deletejob()

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Delete the entries of the historical data imports in the organization.

Deprecated: Please use POST /workforcemanagement/historicaldata/bulk/remove/jobs instead.

Wraps POST /api/v2/workforcemanagement/historicaldata/deletejob 

Requires ALL permissions: 

* wfm:historicalData:upload

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()

try:
    # Delete the entries of the historical data imports in the organization.
    api_response = api_instance.post_workforcemanagement_historicaldata_deletejob()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_historicaldata_deletejob: %s\n" % e)
```

### Parameters

This endpoint does not need any parameters.

### Return type

[**HistoricalImportDeleteJobResponse**](HistoricalImportDeleteJobResponse)


## post_workforcemanagement_historicaldata_validate

> [**ValidationServiceAsyncResponse**](ValidationServiceAsyncResponse) post_workforcemanagement_historicaldata_validate(body=body)


Trigger validation process for historical import

Wraps POST /api/v2/workforcemanagement/historicaldata/validate 

Requires ALL permissions: 

* wfm:historicalData:upload

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.ValidationServiceRequest() # ValidationServiceRequest | body (optional)

try:
    # Trigger validation process for historical import
    api_response = api_instance.post_workforcemanagement_historicaldata_validate(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_historicaldata_validate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**ValidationServiceRequest**](ValidationServiceRequest)| body | [optional]  |

### Return type

[**ValidationServiceAsyncResponse**](ValidationServiceAsyncResponse)


## post_workforcemanagement_integrations_hri_timeofftypes_jobs

> [**HrisTimeOffTypesResponse**](HrisTimeOffTypesResponse) post_workforcemanagement_integrations_hri_timeofftypes_jobs(hris_integration_id)


Get list of time off types configured in integration

Wraps POST /api/v2/workforcemanagement/integrations/hris/{hrisIntegrationId}/timeofftypes/jobs 

Requires ANY permissions: 

* wfm:integration:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
hris_integration_id = 'hris_integration_id_example' # str | The ID of the HRIS integration for which time off types are queried.

try:
    # Get list of time off types configured in integration
    api_response = api_instance.post_workforcemanagement_integrations_hri_timeofftypes_jobs(hris_integration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_integrations_hri_timeofftypes_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **hris_integration_id** | **str**| The ID of the HRIS integration for which time off types are queried. |  |

### Return type

[**HrisTimeOffTypesResponse**](HrisTimeOffTypesResponse)


## post_workforcemanagement_managementunit_agents_workplans_query

> [**AgentsWorkPlansResponse**](AgentsWorkPlansResponse) post_workforcemanagement_managementunit_agents_workplans_query(management_unit_id, force_download_service=force_download_service, body=body)


Get agents work plans configuration

Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/agents/workplans/query 

Requires ANY permissions: 

* wfm:workPlan:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
force_download_service = True # bool | Force the result of this operation to be sent via download service. For testing/app development purposes (optional)
body = PureCloudPlatformClientV2.GetAgentsWorkPlansRequest() # GetAgentsWorkPlansRequest | body (optional)

try:
    # Get agents work plans configuration
    api_response = api_instance.post_workforcemanagement_managementunit_agents_workplans_query(management_unit_id, force_download_service=force_download_service, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_agents_workplans_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **force_download_service** | **bool**| Force the result of this operation to be sent via download service. For testing/app development purposes | [optional]  |
| **body** | [**GetAgentsWorkPlansRequest**](GetAgentsWorkPlansRequest)| body | [optional]  |

### Return type

[**AgentsWorkPlansResponse**](AgentsWorkPlansResponse)


## post_workforcemanagement_managementunit_agentschedules_search

> [**BuAsyncAgentSchedulesSearchResponse**](BuAsyncAgentSchedulesSearchResponse) post_workforcemanagement_managementunit_agentschedules_search(management_unit_id, force_async=force_async, force_download_service=force_download_service, body=body)


Query published schedules for given given time range for set of users

Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/agentschedules/search 

Requires ANY permissions: 

* wfm:publishedSchedule:view
* wfm:schedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
force_async = True # bool | Force the result of this operation to be sent asynchronously via notification. For testing/app development purposes (optional)
force_download_service = True # bool | Force the result of this operation to be sent via download service. For testing/app development purposes (optional)
body = PureCloudPlatformClientV2.BuSearchAgentSchedulesRequest() # BuSearchAgentSchedulesRequest | body (optional)

try:
    # Query published schedules for given given time range for set of users
    api_response = api_instance.post_workforcemanagement_managementunit_agentschedules_search(management_unit_id, force_async=force_async, force_download_service=force_download_service, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_agentschedules_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **force_async** | **bool**| Force the result of this operation to be sent asynchronously via notification. For testing/app development purposes | [optional]  |
| **force_download_service** | **bool**| Force the result of this operation to be sent via download service. For testing/app development purposes | [optional]  |
| **body** | [**BuSearchAgentSchedulesRequest**](BuSearchAgentSchedulesRequest)| body | [optional]  |

### Return type

[**BuAsyncAgentSchedulesSearchResponse**](BuAsyncAgentSchedulesSearchResponse)


## post_workforcemanagement_managementunit_historicaladherencequery

> [**WfmHistoricalAdherenceResponse**](WfmHistoricalAdherenceResponse) post_workforcemanagement_managementunit_historicaladherencequery(management_unit_id, body=body)


Request a historical adherence report

The maximum supported range for historical adherence queries is 31 days, or 7 days with includeExceptions = true

Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/historicaladherencequery 

Requires ANY permissions: 

* wfm:historicalAdherence:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit
body = PureCloudPlatformClientV2.WfmHistoricalAdherenceQuery() # WfmHistoricalAdherenceQuery | body (optional)

try:
    # Request a historical adherence report
    api_response = api_instance.post_workforcemanagement_managementunit_historicaladherencequery(management_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_historicaladherencequery: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit |  |
| **body** | [**WfmHistoricalAdherenceQuery**](WfmHistoricalAdherenceQuery)| body | [optional]  |

### Return type

[**WfmHistoricalAdherenceResponse**](WfmHistoricalAdherenceResponse)


## post_workforcemanagement_managementunit_move

> [**MoveManagementUnitResponse**](MoveManagementUnitResponse) post_workforcemanagement_managementunit_move(management_unit_id, body=body)


Move the requested management unit to a new business unit

Returns status 200 if the management unit is already in the requested business unit

Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/move 

Requires ALL permissions: 

* wfm:managementUnit:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
body = PureCloudPlatformClientV2.MoveManagementUnitRequest() # MoveManagementUnitRequest | body (optional)

try:
    # Move the requested management unit to a new business unit
    api_response = api_instance.post_workforcemanagement_managementunit_move(management_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_move: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **body** | [**MoveManagementUnitRequest**](MoveManagementUnitRequest)| body | [optional]  |

### Return type

[**MoveManagementUnitResponse**](MoveManagementUnitResponse)


## post_workforcemanagement_managementunit_schedules_search

> [**UserScheduleContainer**](UserScheduleContainer) post_workforcemanagement_managementunit_schedules_search(management_unit_id, body=body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Query published schedules for given given time range for set of users

Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/schedules/search 

Requires ANY permissions: 

* wfm:publishedSchedule:view
* wfm:schedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
body = PureCloudPlatformClientV2.UserListScheduleRequestBody() # UserListScheduleRequestBody | body (optional)

try:
    # Query published schedules for given given time range for set of users
    api_response = api_instance.post_workforcemanagement_managementunit_schedules_search(management_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_schedules_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **body** | [**UserListScheduleRequestBody**](UserListScheduleRequestBody)| body | [optional]  |

### Return type

[**UserScheduleContainer**](UserScheduleContainer)


## post_workforcemanagement_managementunit_shrinkage_jobs

> [**WfmHistoricalShrinkageResponse**](WfmHistoricalShrinkageResponse) post_workforcemanagement_managementunit_shrinkage_jobs(management_unit_id, body=body)


Request a historical shrinkage report

The maximum supported range for historical shrinkage queries is up to 32 days. Historical Shrinkage for a given date range can be queried in two modes - granular and aggregated. To see granular shrinkage information, provide granularity in the request body. 

Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/shrinkage/jobs 

Requires ANY permissions: 

* wfm:shrinkage:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit
body = PureCloudPlatformClientV2.WfmHistoricalShrinkageRequest() # WfmHistoricalShrinkageRequest | body (optional)

try:
    # Request a historical shrinkage report
    api_response = api_instance.post_workforcemanagement_managementunit_shrinkage_jobs(management_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_shrinkage_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit |  |
| **body** | [**WfmHistoricalShrinkageRequest**](WfmHistoricalShrinkageRequest)| body | [optional]  |

### Return type

[**WfmHistoricalShrinkageResponse**](WfmHistoricalShrinkageResponse)


## post_workforcemanagement_managementunit_timeofflimits

> [**TimeOffLimit**](TimeOffLimit) post_workforcemanagement_managementunit_timeofflimits(management_unit_id, body=body)


Creates a new time off limit object under management unit.

Only one limit object is allowed under management unit, so an attempt to create second object will fail.

Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/timeofflimits 

Requires ANY permissions: 

* wfm:timeOffLimit:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit.
body = PureCloudPlatformClientV2.CreateTimeOffLimitRequest() # CreateTimeOffLimitRequest | body (optional)

try:
    # Creates a new time off limit object under management unit.
    api_response = api_instance.post_workforcemanagement_managementunit_timeofflimits(management_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_timeofflimits: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit. |  |
| **body** | [**CreateTimeOffLimitRequest**](CreateTimeOffLimitRequest)| body | [optional]  |

### Return type

[**TimeOffLimit**](TimeOffLimit)


## post_workforcemanagement_managementunit_timeofflimits_values_query

> [**QueryTimeOffLimitValuesResponse**](QueryTimeOffLimitValuesResponse) post_workforcemanagement_managementunit_timeofflimits_values_query(management_unit_id, body=body)


Retrieves time off limit related values based on a given set of filters.

Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/timeofflimits/values/query 

Requires ANY permissions: 

* wfm:timeOffLimit:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit.
body = PureCloudPlatformClientV2.QueryTimeOffLimitValuesRequest() # QueryTimeOffLimitValuesRequest | body (optional)

try:
    # Retrieves time off limit related values based on a given set of filters.
    api_response = api_instance.post_workforcemanagement_managementunit_timeofflimits_values_query(management_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_timeofflimits_values_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit. |  |
| **body** | [**QueryTimeOffLimitValuesRequest**](QueryTimeOffLimitValuesRequest)| body | [optional]  |

### Return type

[**QueryTimeOffLimitValuesResponse**](QueryTimeOffLimitValuesResponse)


## post_workforcemanagement_managementunit_timeoffplans

> [**TimeOffPlan**](TimeOffPlan) post_workforcemanagement_managementunit_timeoffplans(management_unit_id, body=body)


Creates a new time off plan

Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/timeoffplans 

Requires ANY permissions: 

* wfm:timeOffPlan:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit
body = PureCloudPlatformClientV2.CreateTimeOffPlanRequest() # CreateTimeOffPlanRequest | body (optional)

try:
    # Creates a new time off plan
    api_response = api_instance.post_workforcemanagement_managementunit_timeoffplans(management_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_timeoffplans: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit |  |
| **body** | [**CreateTimeOffPlanRequest**](CreateTimeOffPlanRequest)| body | [optional]  |

### Return type

[**TimeOffPlan**](TimeOffPlan)


## post_workforcemanagement_managementunit_timeoffrequests

> [**TimeOffRequestList**](TimeOffRequestList) post_workforcemanagement_managementunit_timeoffrequests(management_unit_id, body=body)


Create a new time off request

Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/timeoffrequests 

Requires ANY permissions: 

* wfm:timeOffRequest:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
body = PureCloudPlatformClientV2.CreateAdminTimeOffRequest() # CreateAdminTimeOffRequest | body (optional)

try:
    # Create a new time off request
    api_response = api_instance.post_workforcemanagement_managementunit_timeoffrequests(management_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_timeoffrequests: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **body** | [**CreateAdminTimeOffRequest**](CreateAdminTimeOffRequest)| body | [optional]  |

### Return type

[**TimeOffRequestList**](TimeOffRequestList)


## post_workforcemanagement_managementunit_timeoffrequests_integrationstatus_query

> [**UserTimeOffIntegrationStatusResponseListing**](UserTimeOffIntegrationStatusResponseListing) post_workforcemanagement_managementunit_timeoffrequests_integrationstatus_query(management_unit_id, body=body)


Retrieves integration statuses for a list of time off requests

Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/timeoffrequests/integrationstatus/query 

Requires ANY permissions: 

* wfm:timeOffRequest:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit.
body = PureCloudPlatformClientV2.QueryTimeOffIntegrationStatusRequest() # QueryTimeOffIntegrationStatusRequest | body (optional)

try:
    # Retrieves integration statuses for a list of time off requests
    api_response = api_instance.post_workforcemanagement_managementunit_timeoffrequests_integrationstatus_query(management_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_timeoffrequests_integrationstatus_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit. |  |
| **body** | [**QueryTimeOffIntegrationStatusRequest**](QueryTimeOffIntegrationStatusRequest)| body | [optional]  |

### Return type

[**UserTimeOffIntegrationStatusResponseListing**](UserTimeOffIntegrationStatusResponseListing)


## post_workforcemanagement_managementunit_timeoffrequests_query

> [**TimeOffRequestListing**](TimeOffRequestListing) post_workforcemanagement_managementunit_timeoffrequests_query(management_unit_id, force_download_service=force_download_service, body=body)


Fetches time off requests matching the conditions specified in the request body

Request body requires one of the following: User ID is specified, statuses == [Pending] or date range to be specified and less than or equal to 33 days.  All other fields are filters

Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/timeoffrequests/query 

Requires ANY permissions: 

* wfm:timeOffRequest:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
force_download_service = True # bool | Force the result of this operation to be sent via download service. For testing/app development purposes (optional)
body = PureCloudPlatformClientV2.TimeOffRequestQueryBody() # TimeOffRequestQueryBody | body (optional)

try:
    # Fetches time off requests matching the conditions specified in the request body
    api_response = api_instance.post_workforcemanagement_managementunit_timeoffrequests_query(management_unit_id, force_download_service=force_download_service, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_timeoffrequests_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **force_download_service** | **bool**| Force the result of this operation to be sent via download service. For testing/app development purposes | [optional]  |
| **body** | [**TimeOffRequestQueryBody**](TimeOffRequestQueryBody)| body | [optional]  |

### Return type

[**TimeOffRequestListing**](TimeOffRequestListing)


## post_workforcemanagement_managementunit_timeoffrequests_waitlistpositions_query

> [**WaitlistPositionListing**](WaitlistPositionListing) post_workforcemanagement_managementunit_timeoffrequests_waitlistpositions_query(management_unit_id, body=body)


Retrieves daily waitlist position for a list of time off requests

Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/timeoffrequests/waitlistpositions/query 

Requires ANY permissions: 

* wfm:timeOffRequest:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit.
body = PureCloudPlatformClientV2.QueryWaitlistPositionsRequest() # QueryWaitlistPositionsRequest | body (optional)

try:
    # Retrieves daily waitlist position for a list of time off requests
    api_response = api_instance.post_workforcemanagement_managementunit_timeoffrequests_waitlistpositions_query(management_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_timeoffrequests_waitlistpositions_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit. |  |
| **body** | [**QueryWaitlistPositionsRequest**](QueryWaitlistPositionsRequest)| body | [optional]  |

### Return type

[**WaitlistPositionListing**](WaitlistPositionListing)


## post_workforcemanagement_managementunit_user_timeoffbalance_jobs

> [**TimeOffBalancesResponse**](TimeOffBalancesResponse) post_workforcemanagement_managementunit_user_timeoffbalance_jobs(management_unit_id, user_id, body)


Query time off balances for a given user for specified activity code and dates

Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/users/{userId}/timeoffbalance/jobs 

Requires ANY permissions: 

* wfm:timeOffRequest:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit
user_id = 'user_id_example' # str | The ID of the user
body = PureCloudPlatformClientV2.TimeOffBalanceRequest() # TimeOffBalanceRequest | The request body

try:
    # Query time off balances for a given user for specified activity code and dates
    api_response = api_instance.post_workforcemanagement_managementunit_user_timeoffbalance_jobs(management_unit_id, user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_user_timeoffbalance_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit |  |
| **user_id** | **str**| The ID of the user |  |
| **body** | [**TimeOffBalanceRequest**](TimeOffBalanceRequest)| The request body |  |

### Return type

[**TimeOffBalancesResponse**](TimeOffBalancesResponse)


## post_workforcemanagement_managementunit_user_timeoffrequest_timeoffbalance_jobs

> [**TimeOffBalancesResponse**](TimeOffBalancesResponse) post_workforcemanagement_managementunit_user_timeoffrequest_timeoffbalance_jobs(management_unit_id, user_id, time_off_request_id)


Query time off balances for dates spanned by a given time off request

Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/users/{userId}/timeoffrequests/{timeOffRequestId}/timeoffbalance/jobs 

Requires ANY permissions: 

* wfm:timeOffRequest:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit.
user_id = 'user_id_example' # str | The userId to whom the time off request applies.
time_off_request_id = 'time_off_request_id_example' # str | The time off request id.

try:
    # Query time off balances for dates spanned by a given time off request
    api_response = api_instance.post_workforcemanagement_managementunit_user_timeoffrequest_timeoffbalance_jobs(management_unit_id, user_id, time_off_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_user_timeoffrequest_timeoffbalance_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit. |  |
| **user_id** | **str**| The userId to whom the time off request applies. |  |
| **time_off_request_id** | **str**| The time off request id. |  |

### Return type

[**TimeOffBalancesResponse**](TimeOffBalancesResponse)


## post_workforcemanagement_managementunit_user_timeoffrequests_estimate

> [**EstimateAvailableTimeOffResponse**](EstimateAvailableTimeOffResponse) post_workforcemanagement_managementunit_user_timeoffrequests_estimate(management_unit_id, user_id, body=body)


Estimates available time off for an agent

Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/users/{userId}/timeoffrequests/estimate 

Requires ANY permissions: 

* wfm:timeOffRequest:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit
user_id = 'user_id_example' # str | The id of the user for whom the time off request estimate is requested
body = PureCloudPlatformClientV2.EstimateAvailableTimeOffRequest() # EstimateAvailableTimeOffRequest | body (optional)

try:
    # Estimates available time off for an agent
    api_response = api_instance.post_workforcemanagement_managementunit_user_timeoffrequests_estimate(management_unit_id, user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_user_timeoffrequests_estimate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit |  |
| **user_id** | **str**| The id of the user for whom the time off request estimate is requested |  |
| **body** | [**EstimateAvailableTimeOffRequest**](EstimateAvailableTimeOffRequest)| body | [optional]  |

### Return type

[**EstimateAvailableTimeOffResponse**](EstimateAvailableTimeOffResponse)


## post_workforcemanagement_managementunit_week_shifttrade_match

> [**MatchShiftTradeResponse**](MatchShiftTradeResponse) post_workforcemanagement_managementunit_week_shifttrade_match(management_unit_id, week_date_id, trade_id, body)


Matches a shift trade. This route can only be called by the receiving agent

Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekDateId}/shifttrades/{tradeId}/match 

Requires ANY permissions: 

* wfm:agentShiftTradeRequest:participate

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
week_date_id = '2013-10-20' # date | The start week date of the initiating shift in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
trade_id = 'trade_id_example' # str | The ID of the shift trade to update
body = PureCloudPlatformClientV2.MatchShiftTradeRequest() # MatchShiftTradeRequest | body

try:
    # Matches a shift trade. This route can only be called by the receiving agent
    api_response = api_instance.post_workforcemanagement_managementunit_week_shifttrade_match(management_unit_id, week_date_id, trade_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_week_shifttrade_match: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **week_date_id** | **date**| The start week date of the initiating shift in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **trade_id** | **str**| The ID of the shift trade to update |  |
| **body** | [**MatchShiftTradeRequest**](MatchShiftTradeRequest)| body |  |

### Return type

[**MatchShiftTradeResponse**](MatchShiftTradeResponse)


## post_workforcemanagement_managementunit_week_shifttrades

> [**ShiftTradeResponse**](ShiftTradeResponse) post_workforcemanagement_managementunit_week_shifttrades(management_unit_id, week_date_id, body)


Adds a shift trade

Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekDateId}/shifttrades 

Requires ANY permissions: 

* wfm:agentShiftTradeRequest:participate

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
week_date_id = '2013-10-20' # date | The start week date of the initiating shift in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
body = PureCloudPlatformClientV2.AddShiftTradeRequest() # AddShiftTradeRequest | body

try:
    # Adds a shift trade
    api_response = api_instance.post_workforcemanagement_managementunit_week_shifttrades(management_unit_id, week_date_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_week_shifttrades: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **week_date_id** | **date**| The start week date of the initiating shift in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **body** | [**AddShiftTradeRequest**](AddShiftTradeRequest)| body |  |

### Return type

[**ShiftTradeResponse**](ShiftTradeResponse)


## post_workforcemanagement_managementunit_week_shifttrades_search

> [**SearchShiftTradesResponse**](SearchShiftTradesResponse) post_workforcemanagement_managementunit_week_shifttrades_search(management_unit_id, week_date_id, body, force_download_service=force_download_service)


Searches for potential shift trade matches for the current agent

Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekDateId}/shifttrades/search 

Requires ANY permissions: 

* wfm:agentShiftTradeRequest:participate

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
week_date_id = '2013-10-20' # date | The start week date of the initiating shift in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
body = PureCloudPlatformClientV2.SearchShiftTradesRequest() # SearchShiftTradesRequest | body
force_download_service = True # bool | Force the result of this operation to be sent via download service. For testing/app development purposes (optional)

try:
    # Searches for potential shift trade matches for the current agent
    api_response = api_instance.post_workforcemanagement_managementunit_week_shifttrades_search(management_unit_id, week_date_id, body, force_download_service=force_download_service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_week_shifttrades_search: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **week_date_id** | **date**| The start week date of the initiating shift in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **body** | [**SearchShiftTradesRequest**](SearchShiftTradesRequest)| body |  |
| **force_download_service** | **bool**| Force the result of this operation to be sent via download service. For testing/app development purposes | [optional]  |

### Return type

[**SearchShiftTradesResponse**](SearchShiftTradesResponse)


## post_workforcemanagement_managementunit_week_shifttrades_state_bulk

> [**BulkUpdateShiftTradeStateResponse**](BulkUpdateShiftTradeStateResponse) post_workforcemanagement_managementunit_week_shifttrades_state_bulk(management_unit_id, week_date_id, body, force_async=force_async)


Updates the state of a batch of shift trades

Admin functionality is not supported with \"mine\".

Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/weeks/{weekDateId}/shifttrades/state/bulk 

Requires ANY permissions: 

* wfm:agentShiftTradeRequest:participate
* wfm:shiftTradeRequest:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
week_date_id = '2013-10-20' # date | The start week date of the initiating shift in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd
body = PureCloudPlatformClientV2.BulkShiftTradeStateUpdateRequest() # BulkShiftTradeStateUpdateRequest | body
force_async = True # bool | Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes (optional)

try:
    # Updates the state of a batch of shift trades
    api_response = api_instance.post_workforcemanagement_managementunit_week_shifttrades_state_bulk(management_unit_id, week_date_id, body, force_async=force_async)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_week_shifttrades_state_bulk: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **week_date_id** | **date**| The start week date of the initiating shift in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd |  |
| **body** | [**BulkShiftTradeStateUpdateRequest**](BulkShiftTradeStateUpdateRequest)| body |  |
| **force_async** | **bool**| Force the result of this operation to be sent asynchronously via notification.  For testing/app development purposes | [optional]  |

### Return type

[**BulkUpdateShiftTradeStateResponse**](BulkUpdateShiftTradeStateResponse)


## post_workforcemanagement_managementunit_workplan_copy

> [**WorkPlan**](WorkPlan) post_workforcemanagement_managementunit_workplan_copy(management_unit_id, work_plan_id, body=body)


Create a copy of work plan

Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/workplans/{workPlanId}/copy 

Requires ANY permissions: 

* wfm:workPlan:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
work_plan_id = 'work_plan_id_example' # str | The ID of the work plan to create a copy
body = PureCloudPlatformClientV2.CopyWorkPlan() # CopyWorkPlan | body (optional)

try:
    # Create a copy of work plan
    api_response = api_instance.post_workforcemanagement_managementunit_workplan_copy(management_unit_id, work_plan_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_workplan_copy: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **work_plan_id** | **str**| The ID of the work plan to create a copy |  |
| **body** | [**CopyWorkPlan**](CopyWorkPlan)| body | [optional]  |

### Return type

[**WorkPlan**](WorkPlan)


## post_workforcemanagement_managementunit_workplan_validate

> [**ValidateWorkPlanResponse**](ValidateWorkPlanResponse) post_workforcemanagement_managementunit_workplan_validate(management_unit_id, work_plan_id, expand=expand, body=body)


Validate Work Plan

Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/workplans/{workPlanId}/validate 

Requires ANY permissions: 

* wfm:workPlan:add
* wfm:workPlan:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
work_plan_id = 'work_plan_id_example' # str | The ID of the work plan to validate. For new work plan, use the word 'new' for the ID.
expand = ['expand_example'] # list[str] |  (optional)
body = PureCloudPlatformClientV2.WorkPlanValidationRequest() # WorkPlanValidationRequest | body (optional)

try:
    # Validate Work Plan
    api_response = api_instance.post_workforcemanagement_managementunit_workplan_validate(management_unit_id, work_plan_id, expand=expand, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_workplan_validate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **work_plan_id** | **str**| The ID of the work plan to validate. For new work plan, use the word &#39;new&#39; for the ID. |  |
| **expand** | [**list[str]**](str)|  | [optional] <br />**Values**: messages |
| **body** | [**WorkPlanValidationRequest**](WorkPlanValidationRequest)| body | [optional]  |

### Return type

[**ValidateWorkPlanResponse**](ValidateWorkPlanResponse)


## post_workforcemanagement_managementunit_workplanrotation_copy

> [**WorkPlanRotationResponse**](WorkPlanRotationResponse) post_workforcemanagement_managementunit_workplanrotation_copy(management_unit_id, work_plan_rotation_id, body=body)


Create a copy of work plan rotation

Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/workplanrotations/{workPlanRotationId}/copy 

Requires ANY permissions: 

* wfm:workPlanRotation:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
work_plan_rotation_id = 'work_plan_rotation_id_example' # str | The ID of the work plan rotation to create a copy
body = PureCloudPlatformClientV2.CopyWorkPlanRotationRequest() # CopyWorkPlanRotationRequest | body (optional)

try:
    # Create a copy of work plan rotation
    api_response = api_instance.post_workforcemanagement_managementunit_workplanrotation_copy(management_unit_id, work_plan_rotation_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_workplanrotation_copy: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **work_plan_rotation_id** | **str**| The ID of the work plan rotation to create a copy |  |
| **body** | [**CopyWorkPlanRotationRequest**](CopyWorkPlanRotationRequest)| body | [optional]  |

### Return type

[**WorkPlanRotationResponse**](WorkPlanRotationResponse)


## post_workforcemanagement_managementunit_workplanrotations

> [**WorkPlanRotationResponse**](WorkPlanRotationResponse) post_workforcemanagement_managementunit_workplanrotations(management_unit_id, body=body)


Create a new work plan rotation

Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/workplanrotations 

Requires ANY permissions: 

* wfm:workPlanRotation:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
body = PureCloudPlatformClientV2.AddWorkPlanRotationRequest() # AddWorkPlanRotationRequest | body (optional)

try:
    # Create a new work plan rotation
    api_response = api_instance.post_workforcemanagement_managementunit_workplanrotations(management_unit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_workplanrotations: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **body** | [**AddWorkPlanRotationRequest**](AddWorkPlanRotationRequest)| body | [optional]  |

### Return type

[**WorkPlanRotationResponse**](WorkPlanRotationResponse)


## post_workforcemanagement_managementunit_workplans

> [**WorkPlan**](WorkPlan) post_workforcemanagement_managementunit_workplans(management_unit_id, validation_mode=validation_mode, body=body)


Create a new work plan

Wraps POST /api/v2/workforcemanagement/managementunits/{managementUnitId}/workplans 

Requires ANY permissions: 

* wfm:workPlan:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit, or 'mine' for the management unit of the logged-in user.
validation_mode = 'validation_mode_example' # str | Allows to create work plan even if the validation result is invalid (optional)
body = PureCloudPlatformClientV2.CreateWorkPlan() # CreateWorkPlan | body (optional)

try:
    # Create a new work plan
    api_response = api_instance.post_workforcemanagement_managementunit_workplans(management_unit_id, validation_mode=validation_mode, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunit_workplans: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit, or &#39;mine&#39; for the management unit of the logged-in user. |  |
| **validation_mode** | **str**| Allows to create work plan even if the validation result is invalid | [optional] <br />**Values**: Ignore |
| **body** | [**CreateWorkPlan**](CreateWorkPlan)| body | [optional]  |

### Return type

[**WorkPlan**](WorkPlan)


## post_workforcemanagement_managementunits

> [**ManagementUnit**](ManagementUnit) post_workforcemanagement_managementunits(body=body)


Add a management unit

It may take a minute or two for a new management unit to be available for api operations

Wraps POST /api/v2/workforcemanagement/managementunits 

Requires ALL permissions: 

* wfm:managementUnit:add

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.CreateManagementUnitApiRequest() # CreateManagementUnitApiRequest | body (optional)

try:
    # Add a management unit
    api_response = api_instance.post_workforcemanagement_managementunits(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_managementunits: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateManagementUnitApiRequest**](CreateManagementUnitApiRequest)| body | [optional]  |

### Return type

[**ManagementUnit**](ManagementUnit)


## post_workforcemanagement_notifications_update

> [**UpdateNotificationsResponse**](UpdateNotificationsResponse) post_workforcemanagement_notifications_update(body=body)


Mark a list of notifications as read or unread

Wraps POST /api/v2/workforcemanagement/notifications/update 

Requires no permissions


### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.UpdateNotificationsRequest() # UpdateNotificationsRequest | body (optional)

try:
    # Mark a list of notifications as read or unread
    api_response = api_instance.post_workforcemanagement_notifications_update(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_notifications_update: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**UpdateNotificationsRequest**](UpdateNotificationsRequest)| body | [optional]  |

### Return type

[**UpdateNotificationsResponse**](UpdateNotificationsResponse)


## post_workforcemanagement_schedules

> [**UserScheduleContainer**](UserScheduleContainer) post_workforcemanagement_schedules(body=body)

:::{"alert":"warning","title":"Deprecated","collapsible":false,"autoCollapse":false}
This resource has been deprecated
:::

Get published schedule for the current user

Wraps POST /api/v2/workforcemanagement/schedules 

Requires ANY permissions: 

* wfm:agentSchedule:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.CurrentUserScheduleRequestBody() # CurrentUserScheduleRequestBody | body (optional)

try:
    # Get published schedule for the current user
    api_response = api_instance.post_workforcemanagement_schedules(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_schedules: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CurrentUserScheduleRequestBody**](CurrentUserScheduleRequestBody)| body | [optional]  |

### Return type

[**UserScheduleContainer**](UserScheduleContainer)


## post_workforcemanagement_team_adherence_historical

> [**WfmHistoricalAdherenceResponse**](WfmHistoricalAdherenceResponse) post_workforcemanagement_team_adherence_historical(team_id, body=body)


Request a teams historical adherence report

The maximum supported range for historical adherence queries is 31 days, or 7 days with includeExceptions = true

Wraps POST /api/v2/workforcemanagement/teams/{teamId}/adherence/historical 

Requires ANY permissions: 

* wfm:historicalAdherence:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
team_id = 'team_id_example' # str | The ID of the team
body = PureCloudPlatformClientV2.WfmHistoricalAdherenceQueryForTeams() # WfmHistoricalAdherenceQueryForTeams | body (optional)

try:
    # Request a teams historical adherence report
    api_response = api_instance.post_workforcemanagement_team_adherence_historical(team_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_team_adherence_historical: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **team_id** | **str**| The ID of the team |  |
| **body** | [**WfmHistoricalAdherenceQueryForTeams**](WfmHistoricalAdherenceQueryForTeams)| body | [optional]  |

### Return type

[**WfmHistoricalAdherenceResponse**](WfmHistoricalAdherenceResponse)


## post_workforcemanagement_team_shrinkage_jobs

> [**WfmHistoricalShrinkageResponse**](WfmHistoricalShrinkageResponse) post_workforcemanagement_team_shrinkage_jobs(team_id, body=body)


Request a historical shrinkage report

The maximum supported range for historical shrinkage queries is up to 32 days

Wraps POST /api/v2/workforcemanagement/teams/{teamId}/shrinkage/jobs 

Requires ANY permissions: 

* wfm:shrinkage:view

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
team_id = 'team_id_example' # str | The ID of the team
body = PureCloudPlatformClientV2.WfmHistoricalShrinkageTeamsRequest() # WfmHistoricalShrinkageTeamsRequest | body (optional)

try:
    # Request a historical shrinkage report
    api_response = api_instance.post_workforcemanagement_team_shrinkage_jobs(team_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_team_shrinkage_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **team_id** | **str**| The ID of the team |  |
| **body** | [**WfmHistoricalShrinkageTeamsRequest**](WfmHistoricalShrinkageTeamsRequest)| body | [optional]  |

### Return type

[**WfmHistoricalShrinkageResponse**](WfmHistoricalShrinkageResponse)


## post_workforcemanagement_timeoffbalance_jobs

> [**TimeOffBalancesResponse**](TimeOffBalancesResponse) post_workforcemanagement_timeoffbalance_jobs(body)


Query time off balances for the current user for specified activity code and dates

Wraps POST /api/v2/workforcemanagement/timeoffbalance/jobs 

Requires ANY permissions: 

* wfm:agentTimeOffRequest:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.TimeOffBalanceRequest() # TimeOffBalanceRequest | The request body

try:
    # Query time off balances for the current user for specified activity code and dates
    api_response = api_instance.post_workforcemanagement_timeoffbalance_jobs(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_timeoffbalance_jobs: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**TimeOffBalanceRequest**](TimeOffBalanceRequest)| The request body |  |

### Return type

[**TimeOffBalancesResponse**](TimeOffBalancesResponse)


## post_workforcemanagement_timeofflimits_available_query

> [**AvailableTimeOffResponse**](AvailableTimeOffResponse) post_workforcemanagement_timeofflimits_available_query(body=body)


Queries available time off for the current user

Wraps POST /api/v2/workforcemanagement/timeofflimits/available/query 

Requires ANY permissions: 

* wfm:agentTimeOffRequest:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.AvailableTimeOffRequest() # AvailableTimeOffRequest | body (optional)

try:
    # Queries available time off for the current user
    api_response = api_instance.post_workforcemanagement_timeofflimits_available_query(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_timeofflimits_available_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**AvailableTimeOffRequest**](AvailableTimeOffRequest)| body | [optional]  |

### Return type

[**AvailableTimeOffResponse**](AvailableTimeOffResponse)


## post_workforcemanagement_timeoffrequests

> [**TimeOffRequestResponse**](TimeOffRequestResponse) post_workforcemanagement_timeoffrequests(body=body)


Create a time off request for the current user

Wraps POST /api/v2/workforcemanagement/timeoffrequests 

Requires ANY permissions: 

* wfm:agentTimeOffRequest:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.CreateAgentTimeOffRequest() # CreateAgentTimeOffRequest | body (optional)

try:
    # Create a time off request for the current user
    api_response = api_instance.post_workforcemanagement_timeoffrequests(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_timeoffrequests: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CreateAgentTimeOffRequest**](CreateAgentTimeOffRequest)| body | [optional]  |

### Return type

[**TimeOffRequestResponse**](TimeOffRequestResponse)


## post_workforcemanagement_timeoffrequests_estimate

> [**EstimateAvailableTimeOffResponse**](EstimateAvailableTimeOffResponse) post_workforcemanagement_timeoffrequests_estimate(body=body)


Estimates available time off for current user

Wraps POST /api/v2/workforcemanagement/timeoffrequests/estimate 

Requires ANY permissions: 

* wfm:agentTimeOffRequest:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.EstimateAvailableTimeOffRequest() # EstimateAvailableTimeOffRequest | body (optional)

try:
    # Estimates available time off for current user
    api_response = api_instance.post_workforcemanagement_timeoffrequests_estimate(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_timeoffrequests_estimate: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**EstimateAvailableTimeOffRequest**](EstimateAvailableTimeOffRequest)| body | [optional]  |

### Return type

[**EstimateAvailableTimeOffResponse**](EstimateAvailableTimeOffResponse)


## post_workforcemanagement_timeoffrequests_integrationstatus_query

> [**TimeOffIntegrationStatusResponseListing**](TimeOffIntegrationStatusResponseListing) post_workforcemanagement_timeoffrequests_integrationstatus_query(body=body)


Retrieves integration statuses for a list of current user time off requests

Wraps POST /api/v2/workforcemanagement/timeoffrequests/integrationstatus/query 

Requires ANY permissions: 

* wfm:agentTimeOffRequest:submit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
body = PureCloudPlatformClientV2.CurrentUserTimeOffIntegrationStatusRequest() # CurrentUserTimeOffIntegrationStatusRequest | body (optional)

try:
    # Retrieves integration statuses for a list of current user time off requests
    api_response = api_instance.post_workforcemanagement_timeoffrequests_integrationstatus_query(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->post_workforcemanagement_timeoffrequests_integrationstatus_query: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | [**CurrentUserTimeOffIntegrationStatusRequest**](CurrentUserTimeOffIntegrationStatusRequest)| body | [optional]  |

### Return type

[**TimeOffIntegrationStatusResponseListing**](TimeOffIntegrationStatusResponseListing)


## put_workforcemanagement_agent_integrations_hris

> [**AgentIntegrationsResponse**](AgentIntegrationsResponse) put_workforcemanagement_agent_integrations_hris(agent_id, body)


Update integrations for agent

Wraps PUT /api/v2/workforcemanagement/agents/{agentId}/integrations/hris 

Requires ANY permissions: 

* wfm:agent:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
agent_id = 'agent_id_example' # str | The ID of the agent
body = PureCloudPlatformClientV2.AgentIntegrationsRequest() # AgentIntegrationsRequest | body

try:
    # Update integrations for agent
    api_response = api_instance.put_workforcemanagement_agent_integrations_hris(agent_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->put_workforcemanagement_agent_integrations_hris: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **agent_id** | **str**| The ID of the agent |  |
| **body** | [**AgentIntegrationsRequest**](AgentIntegrationsRequest)| body |  |

### Return type

[**AgentIntegrationsResponse**](AgentIntegrationsResponse)


## put_workforcemanagement_businessunit_timeofflimit_values

> [**BuTimeOffLimitResponse**](BuTimeOffLimitResponse) put_workforcemanagement_businessunit_timeofflimit_values(business_unit_id, time_off_limit_id, body=body)


Sets daily values for a date range of time-off limit object

Note that only limit daily values can be set through API, allocated and waitlisted values are read-only for time-off limit API

Wraps PUT /api/v2/workforcemanagement/businessunits/{businessUnitId}/timeofflimits/{timeOffLimitId}/values 

Requires ANY permissions: 

* wfm:timeOffLimit:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
business_unit_id = 'business_unit_id_example' # str | The ID of the business unit
time_off_limit_id = 'time_off_limit_id_example' # str | The ID of the time-off limit object to set values for
body = PureCloudPlatformClientV2.BuSetTimeOffLimitValuesRequest() # BuSetTimeOffLimitValuesRequest | body (optional)

try:
    # Sets daily values for a date range of time-off limit object
    api_response = api_instance.put_workforcemanagement_businessunit_timeofflimit_values(business_unit_id, time_off_limit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->put_workforcemanagement_businessunit_timeofflimit_values: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **business_unit_id** | **str**| The ID of the business unit |  |
| **time_off_limit_id** | **str**| The ID of the time-off limit object to set values for |  |
| **body** | [**BuSetTimeOffLimitValuesRequest**](BuSetTimeOffLimitValuesRequest)| body | [optional]  |

### Return type

[**BuTimeOffLimitResponse**](BuTimeOffLimitResponse)


## put_workforcemanagement_managementunit_timeofflimit_values

> [**TimeOffLimit**](TimeOffLimit) put_workforcemanagement_managementunit_timeofflimit_values(management_unit_id, time_off_limit_id, body=body)


Sets daily values for a date range of time off limit object

Note that only limit daily values can be set through API, allocated and waitlisted values are read-only for time off limit API

Wraps PUT /api/v2/workforcemanagement/managementunits/{managementUnitId}/timeofflimits/{timeOffLimitId}/values 

Requires ANY permissions: 

* wfm:timeOffLimit:edit

### Example

```{"language":"python"}
import time
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: PureCloud OAuth
PureCloudPlatformClientV2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = PureCloudPlatformClientV2.WorkforceManagementApi()
management_unit_id = 'management_unit_id_example' # str | The ID of the management unit.
time_off_limit_id = 'time_off_limit_id_example' # str | The ID of the time off limit object to set values for
body = PureCloudPlatformClientV2.SetTimeOffLimitValuesRequest() # SetTimeOffLimitValuesRequest | body (optional)

try:
    # Sets daily values for a date range of time off limit object
    api_response = api_instance.put_workforcemanagement_managementunit_timeofflimit_values(management_unit_id, time_off_limit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkforceManagementApi->put_workforcemanagement_managementunit_timeofflimit_values: %s\n" % e)
```

### Parameters


|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **management_unit_id** | **str**| The ID of the management unit. |  |
| **time_off_limit_id** | **str**| The ID of the time off limit object to set values for |  |
| **body** | [**SetTimeOffLimitValuesRequest**](SetTimeOffLimitValuesRequest)| body | [optional]  |

### Return type

[**TimeOffLimit**](TimeOffLimit)


_PureCloudPlatformClientV2 225.0.0_
