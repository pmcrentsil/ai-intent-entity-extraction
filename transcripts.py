# transcripts.py

# Example transcript for testing multi-turn conversation
MULTI_TURN_CONVERSATION = [
    "Customer: Hi, I need help with my account.",
    "Agent: Sure! What seems to be the issue?",
    "Customer: I want to cancel my service.",
    "Agent: May I ask why you are canceling?",
    "Customer: It’s too expensive.",
    "Agent: I see. Your billing date is June 15th 2025.",
    "Customer: Yes, that's correct.",
]


# Testing Transcripts


# MULTI_TURN_CONVERSATION = [
#     "Customer: Hi, I need help with my account.",
#     "Agent: Sure! What seems to be the issue?",
#     "Customer: I want to cancel my service.",
#     "Agent: May I ask why you are canceling?",
#     "Customer: It’s too expensive.",
#     "Agent: I see. Your billing date is 2023-06-15.",
#     "Customer: Yes, that's correct.",
# ]

# Script

# python main.py `
# --intents "cancel service, add service, update service" `
# --entities "customer_name, billing_date" `
# --output-format json




# MULTI_TURN_CONVERSATION = [
#     "Customer: Hi, my internet is not working.",
#     "Agent: I’m sorry to hear that. Have you tried restarting your modem?",
#     "Customer: Yes, I restarted it twice, but nothing changed.",
#     "Agent: I understand. Let me run a diagnostic test on your connection.",
#     "Customer: Okay.",
#     "Agent: I see that your modem is online, but there may be a service outage in your area.",
#     "Customer: Oh, that makes sense. When will it be fixed?",
#     "Agent: Estimated time for resolution is 2 hours.",
#     "Customer: Alright, thank you for checking.",
#     "Agent: No problem. We’ll notify you once it’s resolved.",
# ]

# Script

# python main.py `
# --intents "technical issue, troubleshooting, service outage" `
# --entities "customer_name, outage_status, estimated_resolution_time" `
# --output-format json





# MULTI_TURN_CONVERSATION = [
#     "Customer: Hi, I heard you have a fiber internet plan. I’d like to upgrade.",
#     "Agent: That’s great! I can help you with that. Can I have your account number?",
#     "Customer: Sure, it’s 987654321.",
#     "Agent: I see your current plan is 300 Mbps. Would you like to upgrade to 1 Gbps fiber?",
#     "Customer: Yes, how much would that cost?",
#     "Agent: The new plan is $89.99 per month.",
#     "Customer: Okay, I’d like to proceed with the upgrade.",
#     "Agent: Great! I’ll schedule an installation. When would you be available?",
#     "Customer: How about this Saturday?",
#     "Agent: We have an appointment available from 10 AM to 12 PM. Does that work?",
#     "Customer: Yes, that’s perfect.",
#     "Agent: Your fiber upgrade is scheduled! You’ll receive a confirmation email shortly.",
# ]

# Script

# python main.py `
# --intents "upgrade plan, pricing inquiry, installation scheduling" `
# --entities "customer_name, account_number, new_plan, installation_date" `
# --output-format json








# MULTI_TURN_CONVERSATION = [
#     "Customer: Hi, I received a notification about a login from another state. I didn’t do that.",
#     "Agent: That’s concerning! Let me check your account.",
#     "Customer: Okay.",
#     "Agent: I see a login attempt from Texas. Was this you?",
#     "Customer: No, I live in California.",
#     "Agent: I’ll secure your account by resetting your password.",
#     "Customer: Please do that.",
#     "Agent: Done! You’ll receive an email with instructions.",
#     "Customer: Thanks! Should I do anything else?",
#     "Agent: I recommend enabling two-factor authentication for extra security.",
#     "Customer: Good idea! How do I do that?",
#     "Agent: You can enable it in your account settings under ‘Security’.",
#     "Customer: I’ll do that now. Thanks for your help!",
#     "Agent: You’re welcome! Stay safe.",
# ]

# Script

# python main.py `
# --intents "account security, password reset, unauthorized access" `
# --entities "customer_name, login_location, security_recommendation" `
# --output-format json
