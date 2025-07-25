"""
Chatbot responses for the TextSummarizer application.
This file contains the comprehensive logic for generating responses to user queries
about the TextSummarizer tool, including features, usage instructions, and troubleshooting.

Version: 2.0
Last Updated: April 14, 2025
"""

def get_response(user_message):
    """
    Generate a detailed response based on the user's message.
    
    Args:
        user_message (str): The message from the user
        
    Returns:
        str: The appropriate response matching the user's query
    """
    user_message = user_message.lower().strip()
    
    # ===== GREETING RESPONSES =====
    if any(word in user_message for word in ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening']):
        return 'Hello! Welcome to TextSummarizer. How can I help you with your text summarization needs today?'
    
    # ===== PERSONAL INTERACTIONS =====
    elif 'how are you' in user_message:
        return 'I\'m doing well, thank you for asking! I\'m ready to help you with your summarization needs. What would you like to do today?'
    
    elif any(word in user_message for word in ['thank', 'thanks', 'appreciate', 'grateful']):
        return 'You\'re welcome! I\'m glad I could help. Feel free to ask if you need any more assistance with text summarization or our platform features.'
    
    elif 'goodbye' in user_message or 'bye' in user_message:
        return 'Goodbye! Feel free to come back anytime you need help with text summarization. Have a great day!'
    
    elif 'nice to meet you' in user_message:
        return 'Nice to meet you too! I\'m here to make text summarization easy and efficient for you. How can I help today?'
    
    # ===== GENERAL HELP AND INFORMATION =====
    elif 'help' in user_message:
        return '''I can help you with various aspects of text summarization:
1. Summarizing text from files, URLs, YouTube videos, or direct input
2. Adjusting compression ratios for your preferred summary length
3. Exporting summaries in different formats
4. Understanding our features and how they work
5. Account information and pricing plans

What specific area would you like help with?'''
    
    elif 'what can you do' in user_message or 'capabilities' in user_message:
        return '''I can help you with:
- Explaining how to use TextSummarizer
- Providing information about our summarization methods
- Guiding you through various input options (text, file, URL, YouTube)
- Explaining output formats and export options
- Answering questions about account setup and pricing
- Troubleshooting common issues
- Explaining technical terms and metrics

What would you like to know more about?'''
    
    elif 'getting started' in user_message or 'how to start' in user_message:
        return '''Getting started with TextSummarizer is easy! Here's a quick guide:
1. Choose your input method (paste text, upload a file, enter a URL, or paste a YouTube link)
2. Adjust the compression ratio slider to your preferred summary length
3. Click "Summarize" and wait a few seconds
4. View your summary in your preferred format (plain text, bullet points, or paragraphs)
5. Export the summary if needed

Would you like more details about any of these steps?'''
    
    # ===== FEATURE EXPLANATIONS =====
    elif any(word in user_message for word in ['compression', 'ratio', 'length']):
        return '''The compression ratio is a key feature that controls your summary length:
- It represents how much the original text will be compressed
- A higher ratio (e.g., 80%) produces a shorter summary
- A lower ratio (e.g., 20%) produces a longer, more detailed summary
- You can adjust this using the slider in the interface
- For most general purposes, a ratio between 40-60% works well
- For very technical or complex content, try a lower ratio (30-40%)
- For basic content or when you need just the key points, a higher ratio (70-80%) works better

You can always adjust and regenerate if the summary is too long or too short.'''
    
    elif any(word in user_message for word in ['format', 'export', 'download', 'save']):
        return '''You have several options for exporting your summaries:
1. TXT format - Simple plain text format compatible with any text editor
2. DOCX format - Microsoft Word format with basic formatting preserved
3. PDF format - Portable document format ideal for sharing and printing

To export your summary:
- Click the "Export" button on the summary result page
- Select your preferred format from the dropdown menu
- Wait for the download to complete (usually just a second or two)
- Files are named with the date and a portion of the original title for easy identification

All exported summaries include metadata showing the original source and compression ratio used.'''
    
    elif any(phrase in user_message for phrase in ['view', 'display', 'show', 'output format']):
        return '''You can view your summary in three different formats:
1. Plain Text View: Displays your summary as continuous text, similar to the original but more concise. Best for reading longer summaries.
2. Bullet Point View: Formats each sentence as a separate bullet point, making it easier to scan and review key points. Perfect for presentation prep or study notes.
3. Paragraph View: Organizes your summary into logical paragraphs. This offers a balance between readability and structure.

You can switch between these views using the tabs above your summary. Your preference will be remembered for future sessions if you're logged in.'''
    
    elif any(word in user_message for word in ['rouge', 'score', 'quality', 'metric']):
        return '''ROUGE score is a quality metric for evaluating summarization:
- ROUGE stands for "Recall-Oriented Understudy for Gisting Evaluation"
- It measures the overlap between the original text and the generated summary
- Higher scores (closer to 1.0) indicate better content preservation
- We display ROUGE-1, ROUGE-2, and ROUGE-L scores:
  * ROUGE-1: Measures unigram (single word) overlap
  * ROUGE-2: Measures bigram (two consecutive words) overlap
  * ROUGE-L: Measures the longest common subsequence
- These metrics help you gauge how well the summary captures the original content
- For most general purposes, a ROUGE-L score above 0.4 indicates a good summary
- Technical or specialized content may have lower scores but still be effective summaries

You can view detailed metrics by clicking the "View Metrics" button below your summary.'''
    
    elif 'keyword extraction' in user_message or 'keywords' in user_message:
        return '''Our keyword extraction feature identifies the most important terms in your text:
- Keywords are extracted based on frequency, position, and semantic importance
- Each keyword is assigned a relevance score (0-100%)
- You can see up to 20 keywords for each summary
- Keywords help identify the main topics and concepts in your text
- They're particularly useful for research, SEO, and content analysis
- Premium users can adjust keyword sensitivity and export keyword lists separately
- Keywords are highlighted in the summary text when you hover over them

To access keywords, look for the "Keywords" tab next to your summary results.'''
    
    elif 'language' in user_message or 'multilingual' in user_message:
        return '''TextSummarizer supports multiple languages:
- We currently support 32 languages including English, Spanish, French, German, Chinese, Japanese, Russian, Arabic, and more
- The language is automatically detected from your input text
- Summarization quality is highest for English, Spanish, French, and German
- For other languages, we recommend using a slightly lower compression ratio
- Premium users can force a specific language model even if auto-detection suggests another language
- All UI elements can be displayed in 12 different languages (change this in Settings)
- ROUGE scores may vary by language due to linguistic differences

You can find the full list of supported languages in the Settings menu.'''
    
    elif 'ai model' in user_message or 'algorithm' in user_message or ('how' in user_message and 'work' in user_message):
        return '''TextSummarizer uses advanced NLP and machine learning:
- Our core technology combines extractive and abstractive summarization approaches
- We use a transformer-based architecture specifically optimized for summarization
- The process involves multiple steps:
  1. Text preprocessing and cleaning
  2. Semantic analysis and sentence importance scoring
  3. Redundancy elimination
  4. Coherence optimization
  5. Final summary generation
- We train our models on diverse content across multiple domains for better accuracy
- Our algorithms consider sentence position, term frequency, semantic similarity, and contextual relevance
- Premium users can select between three AI models optimized for different content types:
  * General: Balanced for most content
  * Academic: Optimized for research papers and technical documents
  * News/Media: Optimized for articles and news content

The system continuously improves through machine learning from user feedback.'''
    
    # ===== INPUT TYPES =====
    elif any(word in user_message for word in ['youtube', 'video']):
        return '''Yes, you can summarize YouTube videos:
- Simply paste the YouTube URL in the YouTube tab
- Our system automatically extracts the video transcript
- If the video has multiple language options, you can select your preferred transcript language
- Maximum video length for free users is 15 minutes
- Premium users can summarize videos up to 3 hours long
- For videos without official transcripts, we use our speech recognition system
- The speech recognition works best for clear audio in English, Spanish, French, and German
- You can adjust timestamps in the transcript before summarizing if needed
- Video thumbnails are included in exported summaries for easy reference

Note: For best results, use videos with clear audio and speakers using standard accents.'''
    
    elif any(word in user_message for word in ['file', 'upload', 'document', 'pdf', 'docx']):
        return '''You can upload various file types for summarization:
- Supported formats: PDF, DOCX, TXT, RTF, EPUB, and HTML
- Maximum file size: 16MB for free users, 50MB for premium users
- Just drag and drop your file or click to browse your device
- For PDFs with scanned images, we use OCR technology to extract text
- Tables, charts, and images are noted but not included in the summary
- Complex document formatting may be simplified in the summary
- For password-protected documents, you'll need to remove protection before uploading
- All uploaded files are processed securely and deleted from our servers after 24 hours
- You can batch upload up to 5 files (premium feature) for consecutive processing

For very large documents, consider splitting them into smaller sections for more accurate summaries.'''
    
    elif any(word in user_message for word in ['url', 'website', 'web', 'link']):
        return '''Web page summarization is easy with TextSummarizer:
- Simply paste the URL in the URL tab
- Our system extracts the main content while filtering out navigation, ads, and footers
- We support both news articles and longer-form web content
- Maximum content length: 10,000 words for free users, unlimited for premium
- Dynamic and JavaScript-heavy websites may have limited compatibility
- We handle paywalled content if you're already logged in to the site in your browser
- Summarizing is most effective for article-type content rather than product pages or forums
- Source attribution is automatically included in all summaries
- Website favicon is included in exported summaries for source identification

For best results, make sure the URL leads directly to the content you want to summarize.'''
    
    elif 'text input' in user_message or 'direct input' in user_message or 'paste text' in user_message:
        return '''Direct text input is the quickest way to use TextSummarizer:
- Simply paste or type your text in the main input box
- Maximum text length: 5,000 words for free users, 20,000 for premium
- Rich text formatting is preserved for premium users
- You can edit the text before summarizing to focus on specific sections
- For academic content, you can use markers like [IMPORTANT] to influence the summarization algorithm
- Multiple paragraphs and sections are handled automatically
- Text is processed entirely in your browser for maximum privacy
- You can save frequently used text as templates (premium feature)

This method is perfect for emails, articles, reports, or any text you can copy and paste.'''
    
    # ===== ACCOUNT AND PRICING =====
    elif any(word in user_message for word in ['account', 'register', 'sign', 'login']):
        return '''Creating an account provides several benefits:
- Save your summarization history and access it later
- Sync your settings across devices
- Export unlimited summaries
- Track your usage statistics
- Access premium features (with paid plans)

To create an account:
1. Click the "Register" button in the top right corner
2. Enter your email and create a password
3. Verify your email address
4. Complete your profile (optional)

We offer single sign-on options with Google, Apple, and Microsoft accounts for faster registration. Your data is never shared with third parties.'''
    
    elif any(word in user_message for word in ['price', 'cost', 'subscription', 'plan', 'free', 'premium']):
        return '''We offer flexible pricing options to meet different needs:

1. Free Plan:
   - 5 summaries per day
   - Up to 5,000 words per summary
   - Basic export options (TXT only)
   - 3 view formats
   - Standard summarization model
   - 7-day history

2. Basic Plan ($4.99/month):
   - 30 summaries per day
   - Up to 10,000 words per summary
   - All export options (TXT, DOCX, PDF)
   - 3 view formats
   - Enhanced summarization model
   - 30-day history
   - Priority processing

3. Premium Plan ($9.99/month):
   - Unlimited summaries
   - Up to 20,000 words per summary
   - All export options with custom formatting
   - Advanced features (keyword extraction, sentiment analysis)
   - 3 specialized AI models
   - Unlimited history
   - Batch processing
   - API access

4. Enterprise Plan (Custom pricing):
   - Custom word limits
   - Advanced security features
   - Team management
   - White-label options
   - Dedicated support
   - Custom AI model training

All paid plans offer a 7-day free trial with no credit card required. We also offer annual billing with a 20% discount.'''
    
    # ===== VIEW TYPES =====
    elif any(word in user_message for word in ['bullet', 'point', 'list']):
        return '''The bullet point view offers several advantages:
- Each key sentence appears as a separate bullet point
- Makes scanning through information much faster
- Ideal for creating presentation slides or study notes
- Removes transition phrases to focus on core content
- Makes it easier to identify and extract specific information
- Best for technical content or when you need to quickly grasp main points
- Premium users can customize bullet point style and hierarchy
- Automatic numbering option for sequential information
- Can be toggled with keyboard shortcut Alt+B or Cmd+B
- Particularly useful for summarizing how-to guides and instructional content

You can switch to bullet point view by clicking the "Bullet Points" tab above your summary.'''
    
    elif 'paragraph' in user_message:
        return '''The paragraph view offers a more natural reading experience:
- Organizes your summary into coherent paragraphs
- Preserves the logical flow of the original text
- Adds appropriate transition phrases between ideas
- Best for narrative content, articles, and essays
- Maintains the author's original structure when possible
- Premium users can adjust paragraph length and style
- Provides a more traditional reading experience
- Ideal for longer summaries or when context is important
- Can be toggled with keyboard shortcut Alt+P or Cmd+P
- Works well for summarizing stories, news articles, and opinion pieces

You can switch to paragraph view by clicking the "Paragraphs" tab above your summary.'''
    
    elif any(phrase in user_message for phrase in ['plain', 'text', 'continuous']):
        return '''The plain text view is our simplest format:
- Displays your summary as continuous text
- Similar to the original format but more concise
- No additional formatting or structure added
- Ideal for copying and pasting into other applications
- Best for when you want to further edit the summary yourself
- Preserves any essential formatting from the original (like emphasis)
- Default view for all new summaries
- Most space-efficient view for longer summaries
- Can be toggled with keyboard shortcut Alt+T or Cmd+T
- Perfect for getting a quick overview of lengthy content

You can switch to plain text view by clicking the "Plain Text" tab above your summary.'''
    
    # ===== METRICS AND ANALYTICS =====
    elif any(phrase in user_message for phrase in ['word count', 'character count', 'length']):
        return '''We provide detailed metrics about your summary:
- Word count of both original text and summary
- Character count with and without spaces
- Reading time estimate based on average reading speed (adjustable in settings)
- Compression percentage achieved
- Readability scores using multiple algorithms:
  * Flesch-Kincaid Grade Level
  * Gunning Fog Index
  * SMOG Index
  * Coleman-Liau Index
- Sentiment analysis (positive/negative/neutral percentage)
- Language complexity score
- Technical terminology percentage
- Topic classification

Premium users can access detailed analytics dashboards showing trends across multiple summaries.'''
    
    elif 'readability' in user_message:
        return '''We analyze readability using multiple industry-standard metrics:
- Flesch-Kincaid Grade Level: Indicates the US grade level needed to understand the text
- Gunning Fog Index: Estimates years of formal education needed to understand
- SMOG Index: Measures syllable count and sentence length complexity
- Coleman-Liau Index: Uses characters instead of syllables for better digital text analysis
- Average scores are displayed on a scale of 1-100, with higher scores indicating easier readability
- You can hover over any score for a detailed explanation
- Premium users can set readability targets for their summaries
- The system can automatically adjust summaries to meet specified readability levels

These metrics help ensure your summary is appropriate for your intended audience.'''
    
    elif 'analytics' in user_message or 'statistics' in user_message:
        return '''Premium users have access to comprehensive analytics:
- Summary history charts showing usage patterns
- Average compression ratios across different content types
- Readability trends over time
- Most frequently summarized topics and domains
- Word and character count trends
- Most used export formats and view preferences
- Time saved estimates based on reading speed and summary length
- Heat maps showing which parts of documents are most commonly included in summaries
- Weekly email reports with usage statistics and tips
- Comparative performance against similar users (anonymized)

You can access your analytics dashboard from the user menu in the top right corner.'''
    
    # ===== ADVANCED FEATURES =====
    elif 'sentiment analysis' in user_message:
        return '''Our sentiment analysis feature (premium only) provides emotional context:
- Analyzes the emotional tone of both original text and summary
- Categories include positive, negative, neutral, and mixed
- Provides percentage breakdowns of each sentiment category
- Identifies specific emotion markers (e.g., joy, anger, fear, surprise)
- Compares sentiment between original and summary to ensure tone preservation
- Visualizes sentiment distribution with color-coded highlighting
- Offers sentiment trend analysis for longer texts
- Can be toggled on/off in the settings menu
- Particularly useful for analyzing reviews, feedback, and opinion pieces
- Helps ensure important emotional context isn't lost in summarization

Sentiment analysis can be accessed via the "Analysis" tab next to your summary results.'''
    
    elif 'custom dictionaries' in user_message or 'terminology' in user_message:
        return '''Premium users can create custom terminology dictionaries:
- Upload industry-specific terminology lists
- Create custom dictionaries for different subjects or clients
- Ensure important technical terms are preserved in summaries
- Add custom definitions for specialized terms
- Create abbreviation lists for consistent handling
- Set priority levels for different terms
- Share dictionaries across team accounts
- Import existing glossaries from CSV or Excel files
- Export and manage multiple dictionaries
- Apply different dictionaries to different projects

Custom dictionaries ensure that domain-specific language is handled appropriately during summarization.'''
    
    elif 'batch processing' in user_message:
        return '''Batch processing (premium feature) lets you summarize multiple items at once:
- Upload up to 25 files in a single batch
- Enter multiple URLs for consecutive processing
- Apply the same settings to all items or customize individually
- Schedule batch jobs for off-peak hours
- Receive email notifications when batches are complete
- Download all summaries as a single ZIP file
- Generate comparative reports across multiple documents
- Track batch job progress in real-time
- Pause and resume batch jobs as needed
- Access detailed logs for troubleshooting

This feature is perfect for research projects, content audits, or processing document collections.'''
    
    # ===== TROUBLESHOOTING =====
    elif 'error' in user_message or 'issue' in user_message or 'problem' in user_message:
        return '''If you're experiencing issues, here are some common solutions:
1. For upload errors:
   - Check that your file is under the size limit (16MB free, 50MB premium)
   - Ensure the file isn't password-protected or corrupted
   - Try converting to a different format (e.g., DOCX to PDF)

2. For URL summarization issues:
   - Check that the website allows content scraping
   - Try using the direct article URL rather than a homepage
   - Some sites with heavy JavaScript may not work properly

3. For quality issues:
   - Try adjusting the compression ratio
   - For technical content, use a lower compression ratio
   - Check that the input text is clean and well-formatted

4. For general errors:
   - Clear your browser cache
   - Try a different browser
   - Disable browser extensions that might interfere

If you continue experiencing issues, please contact support with the error code displayed.'''
    
    elif 'limit' in user_message and 'exceed' in user_message:
        return '''If you've exceeded your daily summary limit:
1. Free users are limited to 5 summaries per day
2. Basic users are limited to 30 summaries per day
3. Premium users have unlimited summaries

Your limit resets at midnight UTC. If you frequently reach your limit:
- Consider upgrading your plan for higher limits
- Use batch processing (premium) to maximize efficiency
- Schedule important summarization tasks early in your day
- Save drafts of important text to prioritize summarization tasks

You can check your current usage and limits in the account dashboard.'''
    
    elif 'slow' in user_message or 'performance' in user_message:
        return '''If the summarization process seems slow:
1. Processing time depends on several factors:
   - Text length (longer texts take more time)
   - Input format (PDFs with images take longer)
   - Current server load
   - Your internet connection speed

2. Average processing times:
   - Short texts (under 1000 words): 2-5 seconds
   - Medium texts (1000-5000 words): 5-15 seconds
   - Long texts (5000+ words): 15-60 seconds
   - YouTube videos: Additional 5-10 seconds for transcript extraction

3. Tips for faster processing:
   - Use plain text input when possible
   - Consider splitting very long documents
   - Premium users get priority processing
   - Avoid peak usage times (weekdays 9-5 PM)

If performance issues persist, try clearing your browser cache or using our desktop application.'''
    
    # ===== ABOUT THE CHATBOT =====
    elif ('who' in user_message and ('you' in user_message or 'are' in user_message)) or 'your name' in user_message:
        return '''I'm the TextSummarizer AI assistant, designed to help you with all aspects of our text summarization platform. I can answer questions about:

- How to use our summarization tools
- Different input options and formats
- Account setup and management
- Pricing and feature comparisons
- Technical aspects of our summarization algorithm
- Troubleshooting common issues

I'm constantly being updated with the latest information about our platform. If I can't answer your question directly, I can connect you with our human support team.'''
    
    elif 'made' in user_message or 'created' in user_message or 'developed' in user_message:
        return '''TextSummarizer was developed by a team of NLP specialists and software engineers with expertise in natural language processing and machine learning. The platform was first launched in 2025 and has been continuously improved through user feedback and technological advances. Our team is committed to making text summarization accessible, accurate, and useful for everyone from students to professionals. We're based in San Francisco with team members across North America, Europe, and Asia.'''
    
    # ===== PRIVACY AND SECURITY =====
    elif 'privacy' in user_message or 'data' in user_message or 'security' in user_message:
        return '''We take privacy and security seriously:
- All uploaded content is encrypted in transit and at rest
- Files and extracted text are automatically deleted after 24 hours
- We do not use your content to train our models without explicit consent
- You can request immediate deletion of your data at any time
- We comply with GDPR, CCPA, and other privacy regulations
- Premium users can enable end-to-end encryption for additional security
- We use industry-standard security practices and regular audits
- Our full privacy policy is available at textummarizer.com/privacy
- Enterprise users receive additional security features and custom data retention policies

If you have specific privacy concerns, our privacy team can be reached at privacy@textsummarizer.com.'''
    
    # ===== INTEGRATIONS =====
    elif 'integration' in user_message or 'connect' in user_message or 'api' in user_message:
        return '''TextSummarizer offers several integration options:
- API access for Premium and Enterprise users
- Chrome and Firefox browser extensions
- Microsoft Word and Google Docs plugins
- Zapier and IFTTT connections
- Slack integration for team environments
- Notion integration for knowledge management
- Email summarization via dedicated email address
- Mobile apps for iOS and Android
- Command-line interface for developers
- WebDAV support for content management systems

For technical documentation and API keys, visit our Developer Portal at developer.textsummarizer.com. Enterprise customers can request custom integrations for specific workflows.'''
    
    # ===== DEFAULT RESPONSE =====
    else:
        return '''I'm here to help with all aspects of text summarization. You can ask me about:
- How to use specific features
- Different input and output options
- Account management and pricing
- Technical details about our summarization process
- Troubleshooting common issues

What would you like to know more about?'''