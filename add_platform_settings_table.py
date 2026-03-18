#!/usr/bin/env python3
"""
Migration script to add platform_settings table to existing database
"""
import config

def add_platform_settings_table():
    """Add platform_settings table if it doesn't exist"""
    try:
        conn = config.get_db_connection()
        cursor = conn.cursor()
        
        # Create platform_settings table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS platform_settings (
                id INT AUTO_INCREMENT PRIMARY KEY,
                platform_name VARCHAR(255) NOT NULL DEFAULT 'Rohidas Footwear',
                platform_logo VARCHAR(255),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        """)
        
        # Insert default settings if table is empty
        cursor.execute("SELECT COUNT(*) as count FROM platform_settings")
        result = cursor.fetchone()
        
        if result[0] == 0:
            cursor.execute("""
                INSERT INTO platform_settings (platform_name, platform_logo) 
                VALUES ('Rohidas Footwear', NULL)
            """)
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print("✓ Platform settings table created successfully!")
        print("✓ Default settings inserted")
        return True
        
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return False

if __name__ == '__main__':
    print("Adding platform_settings table...")
    add_platform_settings_table()
